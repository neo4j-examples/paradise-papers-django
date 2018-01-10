from django.db import models
from neomodel import *
from neomodel import db
from django_neomodel import DjangoNode

class Address(DjangoNode):
    sourceID      = StringProperty()
    country_codes = StringProperty()
    valid_until   = StringProperty()
    address       = StringProperty()
    countries     = StringProperty()
    node_id       = StringProperty()

install_labels(Address)
