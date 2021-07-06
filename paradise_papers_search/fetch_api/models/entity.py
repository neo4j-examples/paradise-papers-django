from neomodel import (
    StringProperty,
    StructuredNode,
    RelationshipTo,
    RelationshipFrom,
    Relationship,
    UniqueIdProperty
)
from django_neomodel import DjangoNode

from .nodeutils import NodeUtils


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
    node_id                  = UniqueIdProperty(primary_key=True)
    status                   = StringProperty()
    officers                 = RelationshipFrom('.officer.Officer', 'OFFICER_OF')
    intermediaries           = RelationshipFrom('.intermediary.Intermediary', 'INTERMEDIARY_OF')
    addresses                = RelationshipTo('.address.Address', 'REGISTERED_ADDRESS')
    others                   = RelationshipFrom('.other.Other', 'CONNECTED_TO')
    entities                 = Relationship('.entity.Entity', None)

    class Meta:
        app_label = "fetch_api"

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
                'nodes_related': self.serialize_relationships(self.officers.all()),
            },
            {
                'nodes_type': 'Intermediary',
                'nodes_related': self.serialize_relationships(self.intermediaries.all()),
            },
            {
                'nodes_type': 'Address',
                'nodes_related': self.serialize_relationships(self.addresses.all()),
            },
            {
                'nodes_type': 'Other',
                'nodes_related': self.serialize_relationships(self.others.all()),
            },
            {
                'nodes_type': 'Entity',
                'nodes_related': self.serialize_relationships(self.entities.all())
            },
        ]
