from neomodel import *
from neomodel import db
from django_neomodel import DjangoNode

class Other(DjangoNode):
    sourceID    = StringProperty()
    name        = StringProperty()
    valid_until = StringProperty()
    node_id     = StringProperty()

    @property
    def serialize(self):
        return{
            'node_properties': {
                'sourceID': self.sourceID,
                'name': self.name,
                'valid_until': self.valid_until,
                'node_id': self.node_id,
            },
        }

install_labels(Other)
