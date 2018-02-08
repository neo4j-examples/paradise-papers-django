from neomodel import (
    StringProperty,
    StructuredNode,
    RelationshipTo,
    Relationship
)

from .nodeutils import NodeUtils


class Other(StructuredNode, NodeUtils):
    sourceID    = StringProperty()
    name        = StringProperty()
    valid_until = StringProperty()
    node_id     = StringProperty(index = True)
    countries   = StringProperty()
    addresses   = RelationshipTo('.address.Address', 'REGISTERED_ADDRESS')
    officers    = Relationship('.officer.Officer', None)
    entities    = Relationship('.entity.Entity', None)


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
                'nodes_related': self.serialize_relationships(self.officers.all()),
            },
            {
                'nodes_type': 'Entity',
                'nodes_related': self.serialize_relationships(self.entities.all()),
            },
            {
                'nodes_type': 'Address',
                'nodes_related': self.serialize_relationships(self.addresses.all()),
            },
        ]
