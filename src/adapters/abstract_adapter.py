import abc

class AbstractAdapter(object):

    @abc.abstractmethod
    def call(self, order):
        pass

    def __init__(self, partner_settings):
        self._partner_settings = partner_settings
