from configs.loader import Loader
from configs import config
from src.builders.factory_builder import FactoryBuilder

class FactoryAdapter(object):

    _factory = None

    def __init__(self, builder_factory):
        if not isinstance(builder_factory, FactoryBuilder):
            raise ValueError('Invalid Argument. Must be FactoryBuilder instance')
        self._factory = builder_factory


    def create(self, partner_name):

        settings = Loader.get_partner_settings(partner_name)

        partner_name = self._get_partner_name(partner_name)

        adapters_path = 'src.adapters.%s.adapter' % partner_name
        adapters_module =  __import__(adapters_path, globals(), locals(), ['Adapter'])

        builder = self._factory.create(partner_name, 'response')
        return adapters_module.Adapter(settings, builder)

    def _get_partner_name(self, partner_name):

        if config.get_env() == 'testing' :
            partner_name = 'mock'

        return partner_name
