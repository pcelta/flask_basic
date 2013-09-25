class FactoryValidator(object):
    def create(self, partner_name):
        adapters_path = 'src.validators.%s.validator' % partner_name
        module = __import__(adapters_path, globals(), locals(), ['Adapter'])
        return module.Validator()
