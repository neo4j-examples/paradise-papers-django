from .entity import Entity
from .address import Address
from .intermediary import Intermediary
from .officer import Officer
from .other import Other


MODEL_ENTITIES = {
    'Entity': Entity,
    'Address': Address,
    'Intermediary': Intermediary,
    'Officer': Officer,
    'Other': Other
}
