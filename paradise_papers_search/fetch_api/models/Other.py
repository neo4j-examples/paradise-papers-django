from neomodel import *
from .Extended_Node import ExtendedNode

class Other(StructuredNode, ExtendedNode):
    sourceID    = StringProperty()
    name        = StringProperty()
    valid_until = StringProperty()
    node_id     = StringProperty()
    countries   = StringProperty()
    addresses   = RelationshipTo('.Address.Address', 'REGISTERED_ADDRESS')

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
                'nodes_related': self.serialized_realtionships_of_type('Officer'),
            },
            {
                'nodes_type': 'Entity',
                'nodes_related': self.serialized_realtionships_of_type('Entity'),
            },
            {
                'nodes_type': 'Address',
                'nodes_related': self.serialize_relationships(self.addresses.all(), 'REGISTERED_ADDRESS'),
            },

        ]
