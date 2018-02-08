from neomodel import (
    StringProperty,
    StructuredNode,
    RelationshipTo,
)

from .nodeutils import NodeUtils


class Officer(StructuredNode, NodeUtils):
    sourceID      = StringProperty()
    name          = StringProperty()
    country_codes = StringProperty()
    valid_until   = StringProperty()
    countries     = StringProperty()
    node_id       = StringProperty(index = True)
    addresses     = RelationshipTo('.address.Address', 'REGISTERED_ADDRESS')
    entities      = RelationshipTo('.entity.Entity', 'OFFICER_OF')


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
