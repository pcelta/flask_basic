import abc
from src.builders.interpartner.response import ResponseBuilder

class AbstractAdapter(object):

    _partner_settings   = None
    _builder            = None

    @abc.abstractmethod
    def call(self, order):
        pass

    def __init__(self, partner_settings, builder):
        self._partner_settings = partner_settings
        self._builder = builder
