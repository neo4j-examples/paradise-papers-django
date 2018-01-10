from django.db import models
from neomodel import *
from neomodel import db
from django_neomodel import DjangoNode

#Class for Neo4j databaser nodes
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
    officers                 = RelationshipFrom('.Officer.Officer', 'OFFICER_OF')
    intermediaries           = RelationshipFrom('.Intermediary.Intermediary', 'INTERMEDIARY_OF')
    addressess               = RelationshipTo('.Address.Address', 'REGISTERED_ADDRESS')
    others                   = RelationshipFrom('.Other.Other', 'CONNECTED_TO')

install_labels(Entity)
