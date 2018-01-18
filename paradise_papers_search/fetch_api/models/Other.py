from neomodel import *
from neomodel import db
from django_neomodel import DjangoNode
from . import helpers

class Other(DjangoNode):
    sourceID    = StringProperty()
    name        = StringProperty()
    valid_until = StringProperty()
    node_id     = StringProperty()
    addresses   = RelationshipTo('.Address.Address', 'REGISTERED_ADDRESS')

    @property
    def serialize(self):
        return{
            'node_properties': {
                'sourceID': self.sourceID,
                'name': self.name,
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
                'nodes_related': helpers.serialize_relationships(self.addresses.all(), 'REGISTERED_ADDRESS'),
            },

        ]
