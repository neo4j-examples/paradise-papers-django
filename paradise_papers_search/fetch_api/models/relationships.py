import re

from neomodel import StructuredRel


class ExtendRel:
    """Extend StructuredRel objects with useful properties and methods."""

    @classmethod
    def getLabel(cls):
        """
        Generate label from the class name.

        Split and add urderscore at a capital letter, then convert to uppercase.
        Example: RelClassName --> REL_CLASS_NAME
        """
        return re.sub(r'(?<=[^A-Z_-])([A-Z])', r'_\1', cls.__name__).upper()

    def __repr__(self):
        return self.getLabel()


###############################################################################
# Paradise Paper Relationships mapping
#
# TODO: Map relationship properties(if we decide to use the data.)
# Re: http://neomodel.readthedocs.io/en/latest/relationships.html#properties
###############################################################################

class ConnectedTo(StructuredRel, ExtendRel):
    """Relationship Representation for CONNECTED_TO"""
    pass


class RegisteredAddress(StructuredRel, ExtendRel):
    """Relationship Representation for REGISTERED_ADDRESS"""
    pass


class OfficerOf(StructuredRel, ExtendRel):
    """Relationship Representation for OFFICER_OF"""
    pass


class IntermediaryOf(StructuredRel, ExtendRel):
    """Relationship Representation for INTERMEDIARY_OF"""
    pass


class RegisteredAddress(StructuredRel, ExtendRel):
    """Relationship Representation for REGISTERED_ADDRESS"""
    pass
