import os, sys
from configs import config
from configs.loader import Loader

class FactoryBuilder(object):

    availables_actions = {'activate', 'cancel', 'response'}

    def create(self, partner_name, action):

        if action not in self.availables_actions :
            raise ValueError('Invalid Argument')

        partner_settings = Loader.get_partner_settings(partner_name)
        partner_name = self._get_partner_name(partner_name)
        builders_path = 'src.builders.%s.%s' % (partner_name, action)

        if action == 'activate' :
            module = __import__(builders_path, globals(), locals(), ['ActivateBuilder'])
            return module.ActivateBuilder()

        if action == 'cancel' :
            module = __import__(builders_path, globals(), locals(), ['CancelBuilder'])
            return module.CancelBuilder()

        if action == 'response' :
            module = __import__(builders_path, globals(), locals(), ['ResponseBuilder'])
            return module.ResponseBuilder()

        raise ValueError('Invalid Argument. Action <%s> unknow' % action)

    def _get_partner_name(self, partner_name):

        if config.get_env() == 'testing' :
            partner_name = 'mock'

        return partner_name

