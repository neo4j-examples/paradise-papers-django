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

install_labels(Intermediary)
