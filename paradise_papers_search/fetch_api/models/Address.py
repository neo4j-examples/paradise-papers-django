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

    @property
    def serialize(self):
        return {
            'node_properties': {
                'sourceID': self.sourceID,
                'country_codes': self.country_codes,
                'valid_until': self.valid_until,
                'address': self.address,
                'countries': self.countries,
                'node_id': self.node_id,
            },
        }

install_labels(Address)
