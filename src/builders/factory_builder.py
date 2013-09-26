import os, sys

from configs.loader import Loader

class FactoryBuilder(object):

    availables_actions = {'activate', 'cancel'}

    def create(self, partner_name, action):

        if action not in self.availables_actions :
            raise ValueError('Invalid Argument')

        partner_settings = Loader.get_partner_settings(partner_name)

        builders_path = 'src.builders.%s' % partner_name
        if action == 'activate' :
            module = __import__(builders_path + '.activate', globals(), locals(), ['ActivateBuilder'])
            return module.ActivateBuilder()

