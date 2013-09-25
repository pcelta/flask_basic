import unittest
#import ipdb; ipdb.set_trace()
from src.validators.json_validator import RequestValidator

class TestRequestValidator(unittest.TestCase):

    def test_validate_should_return_true_when_valid_json(self):
        validator = RequestValidator()
        result = validator.validate('{"orders" : [{"purchase" : "1"}]}')
        self.assertTrue(result)

    def test_validate_should_return_false_when_orders_not_exists(self):
        validator = RequestValidator()
        result = validator.validate('{"order" : [{}]}')
        self.assertFalse(result)

    def test_validate_should_return_false_when_orders_is_not_list(self):
        validator = RequestValidator()
        result = validator.validate('{"orders" : "any"}')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

