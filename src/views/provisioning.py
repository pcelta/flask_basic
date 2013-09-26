from src.validators.json_validator import JsonValidator
from src.services.provisioning import ProvisioningService
from src.builders.factory_builder import FactoryBuilder
from src.adapters.factory_adapter import FactoryAdapter

class Provisioning(object):

    validator = None
    provisioning_service = None
    
    def __init__(self, validator, provisioning_service) :
        if not isinstance(validator, JsonValidator) :
            raise ValueError('Invalid Argument. Must be JsonValidator instance')

        if not isinstance(provisioning_service, ProvisioningService) :
            raise ValueError('Invalid Argument. Must be ProvisioningService instance')

        self.validator = validator
        self.provisioning_service = provisioning_service
    
    def activate(self, json):
        if (self.validator.validate(json)) :
            return self.provisioning_service.activate(json)

        return '{"error" : "Invalid JSON"}'

    @staticmethod
    def create():
        provisioning_service = ProvisioningService(FactoryBuilder(), FactoryAdapter())
        return Provisioning(JsonValidator(), provisioning_service)
