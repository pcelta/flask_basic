from src.validators.order_validator import PartnerOrderValidator
from src.builders.factory_builder import FactoryBuilder
from src.adapters.factory_adapter import FactoryAdapter
from src.validators.factory_validator import FactoryValidator
from src.entities.content import Result
from src.builders.response import Response

class ProvisioningService(object):

    _factory_builder   = None
    _factory_adapter   = None
    _factory_validator = None

    def __init__(self, factory_validator, factory_builder, factory_adapter):

        if not isinstance(factory_validator, FactoryValidator):
            raise ValueError('Invalid Argument. Must be FactoryValidator instance')

        if not isinstance(factory_builder, FactoryBuilder):
            raise ValueError('Invalid Argument. Must be FactoryBuilder instance')

        if not isinstance(factory_adapter, FactoryAdapter):
            raise ValueError('Invalid Argument. Must be FactoryAdapter instance')

        self._factory_builder = factory_builder
        self._factory_adapter = factory_adapter
        self._factory_validator = factory_validator

    def activate(self, orders):
        
        for order in orders['orders'] :

            if 'partner' not in order :
                order['result'] = Result.create_with_partner_missing_error('partner')
                continue

            validator = self._factory_validator.create(order['partner'])
            if validator.validate("activate", order) :
                builder = self._factory_builder.create(order['partner'], 'activate')
                adapter = self._factory_adapter.create(order['partner'])
                order['result'] = adapter.call(builder.build(order))
            else :
                order['result'] = Result.create_with_partner_missing_error(validator.get_missing_field())

        builder_reponse = Response()
        return builder_reponse.build(orders)


