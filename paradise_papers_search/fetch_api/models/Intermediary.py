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

install_labels(Intermediary)
