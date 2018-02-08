from neomodel import (
    StringProperty,
    StructuredNode,
    RelationshipFrom
)

from .nodeutils import NodeUtils

class Address(StructuredNode, NodeUtils):
    sourceID      = StringProperty()
    country_codes = StringProperty()
    valid_until   = StringProperty()
    address       = StringProperty()
    countries     = StringProperty()
    node_id       = StringProperty(index = True)
    officers       = RelationshipFrom('.officer.Officer', 'REGISTERED_ADDRESS')
    intermediaries = RelationshipFrom('.intermediary.Intermediary', 'REGISTERED_ADDRESS')


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
                'nodes_related': self.serialize_relationships(self.officers.all(), 'REGISTERED_ADDRESS'),
            },
            {
                'nodes_type': 'Intermediary',
                'nodes_related': self.serialize_relationships(self.intermediaries.all(), 'REGISTERED_ADDRESS'),
            },
    ]

