import unittest
import json
from ....src.validators.order_validator import PartnerOrderValidator, OrderValidator

class Test(unittest.TestCase) :

    def test_validate_should_return_true_when_mandatories_fields_exists_in_json(self):
        order = json.loads('{"purchase" : "1", "contractId" : "", "password" : "xxx", "action" : "incluir", "customerIdentification" : "1" }')
        
        validator = PartnerOrderValidator("")
        result = validator.validate(order)
        self.assertTrue(result)

    def test_validate_should_return_false_when_mandatories_fields_missing(self):
        order = json.loads('{"purchase" : "1", "password" : "xxx", "action" : "incluir", "customerIdentification" : "1" }')
        
        validator = PartnerOrderValidator("")
        result = validator.validate(order)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
