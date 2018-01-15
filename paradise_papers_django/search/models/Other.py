from django.db import models
from neomodel import *
from neomodel import db
from django_neomodel import DjangoNode

class Other(DjangoNode):
    sourceID    = StringProperty()
    name        = StringProperty()
    valid_until = StringProperty()
    node_id     = StringProperty()

install_labels(Other)
