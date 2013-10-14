import os, sys
from configs import config
from configs.loader import Loader

class FactoryBuilder(object):

    availables_actions = {'activate', 'upgrade', 'downgrade', 'cancel', 'response'}

    def create(self, partner_name, action):

        if action not in self.availables_actions :
            raise ValueError('Invalid Argument. Action %s unavailable' % action)

        partner_settings = Loader.get_partner_settings(partner_name)
        partner_name = self._get_partner_name(partner_name)
        builders_path = 'src.builders.%s.%s' % (partner_name, action)

        module = __import__(builders_path, globals(), locals(), ['Builder'])
        return module.Builder()

         
        raise ValueError('Invalid Argument. Action <%s> unknow' % action)

    def _get_partner_name(self, partner_name):

        if config.get_env() == 'testing' :
            partner_name = 'mock'

        return partner_name

