from . import helpers
from .relationships import RegisteredAddress

from neomodel import *
from neomodel import db
from django_neomodel import DjangoNode


class Other(DjangoNode):
    sourceID    = StringProperty()
    name        = StringProperty()
    valid_until = StringProperty()
    node_id     = StringProperty()
    countries   = StringProperty()
    addresses   = RelationshipTo('.Address.Address', RegisteredAddress.getLabel(), model=RegisteredAddress)

    @property
    def serialize(self):
        return{
            'node_properties': {
                'sourceID': self.sourceID,
                'name': self.name,
                'countries': self.countries,
                'valid_until': self.valid_until,
                'node_id': self.node_id,
            },
        }


    @property
    def serialize_connections(self):
        return [
            {
                'nodes_type': 'Officer',
                'nodes_related': helpers.serialized_realtionships_of_type(self, 'Officer'),
            },
            {
                'nodes_type': 'Entity',
                'nodes_related': helpers.serialized_realtionships_of_type(self, 'Entity'),
            },
            {
                'nodes_type': 'Address',
                'nodes_related': helpers.serialize_relationships(self.addresses.all(), RegisteredAddress.getLabel()),
            },

        ]
