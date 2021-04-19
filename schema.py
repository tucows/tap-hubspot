import argparse
import json
import os
import sys
import singer

from singer import RecordMessage, SchemaMessage

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable
from types import MappingProxyType
from tap_hubspot.tap import Taphubspot


from singer_sdk.streams.rest import RESTStream

"""
Description: Module generates schemas for all streams
Usage: python schema.py
"""

output_dir = Path.cwd() / 'tap_hubspot' / 'schemas'

# Update this dictionary to generate new schema and update existing schemas
_streams_props = {
    "broadcasts": "/broadcast/v1/broadcasts",
    "domains": "/cms/v3/domains/",
    "events": "/reports/v2/events",
    "tickets": "/crm-objects/v1/objects/tickets/paged",
    "publishing_channels": "/broadcast/v1/channels/setting/publish/current",

}

class SourceStream(RESTStream):

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return self.config["api_url"]

    def get_url_params(
        self,
        partition: Optional[dict],
        next_page_token: Optional[Any] = None
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization.

        If paging is supported, developers may override this method with specific paging
        logic.
        """
        params = {}
        params["hapikey"] = self.config.get("hapikey")
        starting_datetime = self.get_starting_timestamp(partition)
        if starting_datetime:
            params["updated"] = starting_datetime
        return params

    def post_process(self, row: dict, partition: Optional[dict] = None) -> dict:
        """As needed, append or transform raw data to match expected structure."""
        if 'results' in row:
            return row['results'][0]
        else:
            return row


tap = Taphubspot()
STDOUT = sys.stdout
try:
    for name, path in _streams_props.items():
        with open(f'{output_dir}/{name}.json', 'w') as schema_fd, \
                    open('data.json', 'w') as sample_data:
            sys.stdout = sample_data
            for record in SourceStream(tap, name=name, path=path,).request_records(None):
                if 'results' in record:
                    singer.write_record(name, record['results'][0])
                else:
                    singer.write_record(name, record)
            # Generate schema from sample dataset
            os.system(f'singer-infer-schema < data.json > {output_dir}/{name}.json')
finally:
    sys.stdout = STDOUT