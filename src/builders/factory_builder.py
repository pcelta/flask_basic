import os, sys

from configs.loader import Loader

class FactoryBuilder(object):

    partner_name = ''
    
    availables_actions = {'activate', 'cancel'}

    def __init__(self, partner_name):
        self.partner_name = partner_name

    def create(self, action):

        if action not in self.availables_actions :
            raise ValueError('Invalid Argument')

        partner_settings = Loader.get_partner_settings(self.partner_name)

        builders_path = 'src.builders.%s' % self.partner_name
        if action == 'activate' :
            module = __import__(builders_path + '.activate', globals(), locals(), ['ActivateBuilder'])
            return module.ActivateBuilder()

