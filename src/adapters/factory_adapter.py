from configs import config

class FactoryAdapter(object):

    def create(self, partner_name):
        module = self._get_adapter_module(partner_name)
        global_settings = config.get_configs()
        return module.Adapter(global_settings['partners'][partner_name])

    def _get_adapter_module(self, partner_name):

        if config.get_env() == 'testing' :
            partner_name = 'mock'

        adapters_path = 'src.adapters.%s.adapter' % partner_name
        return __import__(adapters_path, globals(), locals(), ['Adapter'])

            
