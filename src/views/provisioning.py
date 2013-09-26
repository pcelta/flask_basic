from src.validators.json_validator import JsonValidator
from src.services.provisioning import ProvisioningService

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
    
    def provision(self, json):
        if (self.validator.validate(json)) :
            return self.provisioning_service.activate(json)
        else :
            return '{"error" : "Invalid JSON"}'
