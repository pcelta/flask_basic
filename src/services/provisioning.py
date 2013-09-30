from src.validators.order_validator import PartnerOrderValidator
from src.builders.factory_builder import FactoryBuilder
from src.adapters.factory_adapter import FactoryAdapter
from src.entities.content import Result

class ProvisioningService(object):

    factory_builder = None
    factory_adapter = None
    
    def __init__(self, factory_builder, factory_adapter):

        if not isinstance(factory_builder, FactoryBuilder):
            raise ValueError('Invalid Argument. Must be FactoryBuilder instance')

        if not isinstance(factory_adapter, FactoryAdapter):
            raise ValueError('Invalid Argument. Must be FactoryAdapter instance')

        self.factory_builder = factory_builder
        self.factory_adapter = factory_adapter

    def activate(self, json):
        for order in json['orders'] :
            if 'partner' is not order :
                continue

            validator = PartnerOrderValidator(order['partner'])
            if validator.validate(order) :
                builder = self.factory_builder.create(order['partner'], 'activate')
                adapter = self.factory_adapter.create(order['partner'])
                result = adapter.call(builder.build(order))
            else :
                order['result'] = Result.create_with_partner_missing_error()


