from . import helpers
from .relationships import RegisteredAddress, OfficerOf

from neomodel import *
from neomodel import db
from django_neomodel import DjangoNode
from django_neomodel import DjangoNode


class Officer(DjangoNode):
    sourceID      = StringProperty()
    name          = StringProperty()
    country_codes = StringProperty()
    valid_until   = StringProperty()
    countries     = StringProperty()
    node_id       = StringProperty()
    addresses     = RelationshipTo('.Address.Address', RegisteredAddress.getLabel(), model=RegisteredAddress)
    entities      = RelationshipTo('.Entity.Entity', OfficerOf.getLabel(), model=OfficerOf)


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
                'nodes_related': helpers.serialize_relationships(self.addresses.all(), RegisteredAddress.getLabel()),
            },
            {
                'nodes_type': 'Entity',
                'nodes_related': helpers.serialize_relationships(self.entities.all(), OfficerOf.getLabel()),
            },
            {
                'nodes_type': 'Officer',
                'nodes_related': helpers.serialized_realtionships_of_type(self, 'Officer'),
            },
        ]
