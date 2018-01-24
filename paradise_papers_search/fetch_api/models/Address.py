from . import helpers
from .relationships import RegisteredAddress

from neomodel import *
from neomodel import db
from django_neomodel import DjangoNode


class Address(DjangoNode):
    sourceID      = StringProperty()
    country_codes = StringProperty()
    valid_until   = StringProperty()
    address       = StringProperty()
    countries     = StringProperty()
    node_id       = StringProperty()
    officers       = RelationshipFrom('.Officer.Officer', RegisteredAddress.getLabel(), model=RegisteredAddress)
    intermediaries = RelationshipFrom('.Intermediary.Intermediary', RegisteredAddress.getLabel(), model=RegisteredAddress)


    @property
    def serialize(self):
        return {
            'node_properties': {
                'sourceID': self.sourceID,
                'country_codes': self.country_codes,
                'valid_until': self.valid_until,
                'address': self.address,
                'countries': self.countries,
                'node_id': self.node_id,
            },
        }


    @property
    def serialize_connections(self):
        return [
            {
                'nodes_type': 'Officer',
                'nodes_related': helpers.serialize_relationships(self.officers.all(), RegisteredAddress.getLabel()),
            },
            {
                'nodes_type': 'Intermediary',
                'nodes_related': helpers.serialize_relationships(self.intermediaries.all(), RegisteredAddress.getLabel()),
            },
    ]
