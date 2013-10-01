from src.validators.json_validator import JsonValidator
from src.services.provisioning import ProvisioningService
from src.builders.factory_builder import FactoryBuilder
from src.adapters.factory_adapter import FactoryAdapter
import json

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
    
    def activate(self, str_json):
        if (self.validator.validate(str_json)) :
            converted_json = json.loads(str_json)
            response = self.provisioning_service.activate(converted_json)
            return json.dumps(response)

        return '{"error" : "Invalid JSON"}'

    @staticmethod
    def create():
        builder_factory = FactoryBuilder()
        provisioning_service = ProvisioningService(builder_factory, FactoryAdapter(builder_factory))
        return Provisioning(JsonValidator(), provisioning_service)
