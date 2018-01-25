from neomodel import *
from .Extended_Node import ExtendedNode

class Officer(StructuredNode, ExtendedNode):
    sourceID      = StringProperty()
    name          = StringProperty()
    country_codes = StringProperty()
    valid_until   = StringProperty()
    countries     = StringProperty()
    node_id       = StringProperty()
    addresses     = RelationshipTo('.Address.Address', 'REGISTERED_ADDRESS')
    entities      = RelationshipTo('.Entity.Entity', 'OFFICER_OF')

    @property
    def serialize(self):
        return {
            'node_properties': {
                'sourceID': self.sourceID,
                'name': self.name,
                'country_codes': self.country_codes,
                'valid_until': self.valid_until,
                'countries': self.countries,
                'node_id': self.node_id,
            },
        }

    @property
    def serialize_connections(self):
        return [
            {
                'nodes_type': 'Address',
                'nodes_related': self.serialize_relationships(self.addresses.all(), 'REGISTERED_ADDRESS'),
            },
            {
                'nodes_type': 'Entity',
                'nodes_related': self.serialize_relationships(self.entities.all(), 'OFFICER_OF'),
            },
            {
                'nodes_type': 'Officer',
                'nodes_related': self.serialized_realtionships_of_type('Officer'),
            },
        ]
