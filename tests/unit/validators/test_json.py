import unittest
#import ipdb; ipdb.set_trace()
from ....src.validators.json_validator import JsonValidator

class TestJson(unittest.TestCase):

    def test_validate(self):
        validator = JsonValidator()
        result = validator.validate('lala')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()