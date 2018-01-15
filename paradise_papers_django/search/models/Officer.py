from django.db import models
from neomodel import *
from neomodel import db
from django_neomodel import DjangoNode

class Officer(DjangoNode):
    sourceID      = StringProperty()
    name          = StringProperty()
    country_codes = StringProperty()
    valid_until   = StringProperty()
    countries     = StringProperty()
    node_id       = StringProperty()
    addresses     = RelationshipTo('.Address.Address', 'REGISTERED_ADDRESS')
    entities      = RelationshipTo('.Entity.Entity', 'OFFICER_OF')

install_labels(Officer)
