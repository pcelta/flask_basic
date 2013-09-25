class FactoryAdapter(object):

    def create(self, partner_name):
        adapters_path = 'src.adapters.%s.adapter' % partner_name
        module = __import__(adapters_path, globals(), locals(), ['Adapter'])
        return module.Adapter()
