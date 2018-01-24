from . import helpers
from .relationships import IntermediaryOf, RegisteredAddress, OfficerOf

from neomodel import *
from neomodel import db
from django_neomodel import DjangoNode


class Intermediary(DjangoNode):
    sourceID      = StringProperty()
    valid_until   = StringProperty()
    name          = StringProperty()
    country_codes = StringProperty()
    countries     = StringProperty()
    node_id       = StringProperty()
    status        = StringProperty()
    entities      = RelationshipTo('.Entity.Entity', IntermediaryOf.getLabel(), model=IntermediaryOf)
    addresses     = RelationshipTo('.Address.Address', RegisteredAddress.getLabel(), model=RegisteredAddress)
    officers      = Relationship('.Officer.Officer', '*')
    officers_officer_of   = RelationshipFrom('.Officer.Officer', OfficerOf.getLabel(), model=OfficerOf)


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
                'nodes_related': helpers.serialize_relationships(self.entities.all(), IntermediaryOf.getLabel()),
            },
            {
                'nodes_type': 'Address',
                'nodes_related': helpers.serialize_relationships(self.addresses.all(), RegisteredAddress.getLabel()),
            },
            {
                'nodes_type': 'Officer',
                'nodes_related': helpers.serialized_realtionships_of_type(self, 'Officer'),
            },

        ]
