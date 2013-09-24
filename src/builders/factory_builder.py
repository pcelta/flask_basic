import os, sys

sys.path.append(os.path.abspath(os.path.curdir) +'/../../configs')

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
        current_dir = os.path.abspath(os.path.curdir)
        sys.path.append(current_dir + '/' + partner_settings['internal_name'])
        
        if action == 'activate' :
            import activate
            return Activate()

