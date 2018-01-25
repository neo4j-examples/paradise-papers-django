from neomodel import *
from .Extended_Node import ExtendedNode

class Entity(StructuredNode, ExtendedNode):
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
    officers                 = RelationshipFrom('.Officer.Officer', 'OFFICER_OF')
    intermediaries           = RelationshipFrom('.Intermediary.Intermediary', 'INTERMEDIARY_OF')
    addresses                = RelationshipTo('.Address.Address', 'REGISTERED_ADDRESS')
    others                   = RelationshipFrom('.Other.Other', 'CONNECTED_TO')

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
                'nodes_related': self.serialize_relationships(self.officers.all(), 'OFFICER_OF'),
            },
            {
                'nodes_type': 'Intermediary',
                'nodes_related': self.serialize_relationships(self.intermediaries.all(), 'INTERMEDIARY_OF'),
            },
            {
                'nodes_type': 'Address',
                'nodes_related': self.serialize_relationships(self.addresses.all(), 'REGISTERED_ADDRESS'),
            },
            {
                'nodes_type': 'Other',
                'nodes_related': self.serialize_relationships(self.others.all(), 'CONNECTED_TO'),
            },
            {
                'nodes_type': 'Entity',
                'nodes_related': self.serialized_realtionships_of_type('Entity'),
            },
        ]
