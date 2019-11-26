"""Competition Model."""

from config.database import Model


class Competition(Model):
    """Competition Model."""
    __table__ = 'competition'
    __fillable__ = ['name', 'description']
