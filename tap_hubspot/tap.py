"""hubspot tap class."""

import json

from pathlib import Path
from typing import List

from singer_sdk import Tap, Stream
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

# TODO: Import your custom stream types here:
from tap_hubspot.streams import (
    hubspotStream,

    BroadcastsStream,
    DomainsStream,
    EventsStream,
    PublishingChannelsStream,

)


# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    BroadcastsStream,
    DomainsStream,
    EventsStream,
    PublishingChannelsStream,
]

with open("config.json") as config_file:
    data = json.load(config_file)

class Taphubspot(Tap):
    """hubspot tap class."""

    name = "tap-hubspot"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = PropertiesList(
        Property("hapikey", StringType, required=True, default=data['hapikey']),
        Property("start_date", DateTimeType),
        Property("api_url", StringType, default=data['api_url']),
    ).to_dict()


    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


# CLI Execution:

cli = Taphubspot.cli
