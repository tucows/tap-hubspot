"""Stream class for tap-hubspot."""


import requests


from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk.streams import RESTStream

from singer_sdk.typing import (
    ArrayType,
    BooleanType,
    DateTimeType,
    IntegerType,
    NumberType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

class hubspotStream(RESTStream):
    """hubspot stream class."""

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return self.config["api_url"]

    # Alternatively, use a static string for url_base:
    # url_base = "https://api.hubspot.com"

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

# TODO: - Copy-paste as many times as needed to create multiple stream types.

class BroadcastsStream(hubspotStream):
    name = "broadcasts"
    path = "/broadcast/v1/broadcasts"
    primary_keys = ["broadcastGuid"]
    replication_key = "userUpdatedAt"
    schema_filepath = SCHEMAS_DIR / "broadcasts.json"

class DomainsStream(hubspotStream):
    name = "domains"
    path = "/cms/v3/domains/"
    primary_keys = ["id"]
    replication_key = "updatedAt"
    schema_filepath = SCHEMAS_DIR / "domains.json"

class EventsStream(hubspotStream):
    name = "events"
    path = "/reports/v2/events"
    primary_keys = ["id"]
    replication_key = "id"
    schema_filepath = SCHEMAS_DIR / "events.json"

class PublishingChannelsStream(hubspotStream):
    name = "publishing_channels"
    path = "/broadcast/v1/channels/setting/publish/current"
    primary_keys = ["channelId"]
    replication_key = "updatedAt"
    schema_filepath = SCHEMAS_DIR / "publishing_channels.json"

class TicketsStream(hubspotStream):
    name = "tickets"
    path = "/crm-objects/v1/objects/tickets/paged"
    primary_keys = ["objectId"]
    replication_key = "objectId"
    schema_filepath = SCHEMAS_DIR / "publishing_channels.json"

