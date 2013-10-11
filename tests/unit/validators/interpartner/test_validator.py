import unittest
import json
from src.validators.interpartner.validator import Validator

class TestInterpartnerValidator(unittest.TestCase):

    def test_validate_should_return_true_when_mandatories_fields_exists_in_json(self):
        converted_json = json.loads('{"partner" : "interpartner","purchase" : "1", "contractId" : "", "password" : "xxx", "action" : "incluir", "customerIdentification" : "1", "planCode" : "001", "startDate": "", "endDate" : "", "callback" : ""}') 
        
        validator = Validator()
        result = validator.validate("activate", converted_json)
        self.assertTrue(result)

    def test_validate_should_return_false_when_mandatories_fields_missing(self):
        order = json.loads('{"purchase" : "1", "password" : "xxx", "action" : "incluir", "customerIdentification" : "1" }')
        
        validator = Validator()
        result = validator.validate('activate', order)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
