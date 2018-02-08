from neomodel import (
    StringProperty,
    StructuredNode,
    RelationshipTo,
    Relationship
)

from .nodeutils import NodeUtils


class Intermediary(StructuredNode, NodeUtils):
    sourceID      = StringProperty()
    valid_until   = StringProperty()
    name          = StringProperty()
    country_codes = StringProperty()
    countries     = StringProperty()
    node_id       = StringProperty(index = True)
    status        = StringProperty()
    entities      = RelationshipTo('.entity.Entity', 'INTERMEDIARY_OF')
    addresses     = RelationshipTo('.address.Address', 'REGISTERED_ADDRESS')
    officers      = Relationship('.officer.Officer', None)


    @property
    def serialize(self):
        return {
            'node_properties': {
                'sourceID': self.sourceID,
                'valid_until': self.valid_until,
                'name': self.name,
                'country_codes': self.country_codes,
                'countries': self.countries,
                'node_id': self.node_id,
                'status': self.status,
            },
        }


    @property
    def serialize_connections(self):
        return [
            {
                'nodes_type': 'Entity',
                'nodes_related': self.serialize_relationships(self.entities.all()),
            },
            {
                'nodes_type': 'Address',
                'nodes_related': self.serialize_relationships(self.addresses.all()),
            },
            {
                'nodes_type': 'Officer',
                'nodes_related': self.serialize_relationships(self.officers.all()),
            },
        ]
