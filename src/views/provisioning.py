import json

from src.validators.json_validator import JsonValidator
from src.services.provisioning import Provisioner
from src.provisioners.factory_provisioner import FactoryProvisioner

class Provisioning(object):

    _validator = None
    _service = None

    def __init__(self, validator, service) :
        if not isinstance(validator, JsonValidator) :
            raise ValueError('Invalid Argument. Must be JsonValidator instance')

        if not isinstance(service, Provisioner) :
            raise ValueError('Invalid Argument. Must be Provisioner instance')

        self._validator         = validator
        self._service   = service
    
    def activate(self, str_json):
        if (self._validator.validate(str_json)) :
            orders = json.loads(str_json)
            response = self._service.activate(orders)
            return json.dumps(response)

        return '{"error" : "Invalid JSON"}'

    def upgrade(self, str_json):
        if (self._validator.validate(str_json)) :
            orders = json.loads(str_json)
            response = self._service.upgrade(orders)
            return json.dumps(response)

        return '{"error" : "Invalid JSON"}'

    def downgrade(self, str_json):
        if (self._validator.validate(str_json)) :
            orders = json.loads(str_json)
            response = self._service.downgrade(orders)
            return json.dumps(response)

        return '{"error" : "Invalid JSON"}'

    def cancel(self, str_json):
        if (self._validator.validate(str_json)) :
            orders = json.loads(str_json)
            response = self._service.cancel(orders)
            return json.dumps(response)

        return '{"error" : "Invalid JSON"}'

    @staticmethod
    def create():
        factory_provisioner = FactoryProvisioner()
        return Provisioning(JsonValidator(), Provisioner(factory_provisioner))
