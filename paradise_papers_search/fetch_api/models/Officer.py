from neomodel import *
from neomodel import db
from django_neomodel import DjangoNode
from django_neomodel import DjangoNode
from . import helpers

class Officer(DjangoNode):
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
                'nodes_type': 'address',
                'nodes_related': helpers.serialize_relationship(self.addresses.all(), 'REGISTERED_ADDRESS'),
            },
            {
                'nodes_type': 'entity',
                'nodes_related': helpers.serialize_relationship(self.entities.all(), 'OFFICER_OF'),
            },
        ]

install_labels(Officer)