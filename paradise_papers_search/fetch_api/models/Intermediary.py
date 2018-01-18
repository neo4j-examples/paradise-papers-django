from neomodel import *
from neomodel import db
from django_neomodel import DjangoNode
from . import helpers

class Intermediary(DjangoNode):
    sourceID      = StringProperty()
    valid_until   = StringProperty()
    name          = StringProperty()
    country_codes = StringProperty()
    countries     = StringProperty()
    node_id       = StringProperty()
    status        = StringProperty()
    entities      = RelationshipTo('.Entity.Entity', 'INTERMEDIARY_OF')
    addresses     = RelationshipTo('.Address.Address', 'REGISTERED_ADDRESS')

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
                'nodes_related': helpers.serialize_relationships(self.entities.all(), 'INTERMEDIARY_OF'),
            },
            {
                'nodes_type': 'Address',
                'nodes_related': helpers.serialize_relationships(self.addresses.all(), 'REGISTERED_ADDRESS'),
            },
            {
                'nodes_type': 'Officer',
                'nodes_related': helpers.serialized_realtionships_of_type(self, 'Officer'),
            },

        ]
