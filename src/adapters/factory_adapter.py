from configs import config

class FactoryAdapter(object):

    def create(self, partner_name):
        adapters_path = 'src.adapters.%s.adapter' % partner_name
        module = __import__(adapters_path, globals(), locals(), ['Adapter'])
        global_settings = config.get_configs()
        return module.Adapter(global_settings['partners'][partner_name])
