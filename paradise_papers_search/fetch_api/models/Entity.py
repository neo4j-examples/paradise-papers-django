from . import helpers
from .relationships import RegisteredAddress, OfficerOf, IntermediaryOf, ConnectedTo

from neomodel import *
from neomodel import db
from neomodel.match import Traversal
from django_neomodel import DjangoNode


class Entity(DjangoNode):
    sourceID                 = StringProperty()
    address                  = StringProperty()
    jurisdiction             = StringProperty()
    service_provider         = StringProperty()
    countries                = StringProperty()
    jurisdiction_description = StringProperty()
    valid_until              = StringProperty()
    ibcRUC                   = StringProperty()
    name                     = StringProperty()
    country_codes            = StringProperty()
    incorporation_date       = StringProperty()
    node_id                  = StringProperty()
    status                   = StringProperty()
    officers                 = RelationshipFrom('.Officer.Officer', OfficerOf.getLabel(), model=OfficerOf)
    intermediaries           = RelationshipFrom('.Intermediary.Intermediary', IntermediaryOf.getLabel(), model=IntermediaryOf)
    addresses                = RelationshipTo('.Address.Address', RegisteredAddress.getLabel(), model=RegisteredAddress)
    others                   = RelationshipFrom('.Other.Other', ConnectedTo.getLabel(), model=ConnectedTo)
    entities                 = Relationship('.Entity.Entity', '*')


    def connections(self, relmodel=None):
        reltype = relmodel if relmodel is None else relmodel.getLabel()
        rel = Relationship(helpers.MODEL_ENTITIES['Intermediary'], '*')
        # rel._lookup_node_class()
        # return Traversal(self, self.__label__, rel.definition)
        return rel.build_manager(self, self.__label__)


    @property
    def serialize(self):
        return {
            'node_properties': {
                'sourceID': self.sourceID,
                'address': self.address,
                'jurisdiction': self.jurisdiction,
                'service_provider': self.service_provider,
                'countries': self.countries,
                'jurisdiction_description': self.jurisdiction_description,
                'valid_until': self.valid_until,
                'ibcRUC': self.ibcRUC,
                'name': self.name,
                'country_codes': self.country_codes,
                'incorporation_date': self.incorporation_date,
                'node_id': self.node_id,
                'status': self.status,
            },
        }


    @property
    def serialize_connections(self):
        return [
            {
                'nodes_type': 'Officer',
                'nodes_related': helpers.serialize_relationships(self.officers.all(), OfficerOf.getLabel()),
            },
            {
                'nodes_type': 'Intermediary',
                'nodes_related': helpers.serialize_relationships(self.intermediaries.all(), IntermediaryOf.getLabel()),
            },
            {
                'nodes_type': 'Address',
                'nodes_related': helpers.serialize_relationships(self.addresses.all(), RegisteredAddress.getLabel()),
            },
            {
                'nodes_type': 'Other',
                'nodes_related': helpers.serialize_relationships(self.others.all(), ConnectedTo.getLabel()),
            },
            {
                'nodes_type': 'Entity',
                'nodes_related': helpers.serialized_realtionships_of_type(self, 'Entity'),
            },
        ]
