from src.builders.factory_builder import FactoryBuilder
from src.adapters.factory_adapter import FactoryAdapter
from src.validators.factory_validator import FactoryValidator

class FactoryProvisioner(object):

    def create(self, partner_name):
        provisioners_base_path = "src.provisioners.%s.provisioner"
        try :
            provisioners_path = "src.provisioners.%s.provisioner" % partner_name
            module = __import__(provisioners_path, globals(), locals(), ['Provisioner'])

        except(ImportError) :
            provisioners_path = "src.provisioners.generic.provisioner"
            module = __import__(provisioners_path, globals(), locals(), ['Provisioner'])

        factory_builder = FactoryBuilder()
        factory_adapter = FactoryAdapter(factory_builder)
        factory_validator = FactoryValidator()

        return module.Provisioner(factory_builder, factory_adapter, factory_validator)
