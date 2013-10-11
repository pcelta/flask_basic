import unittest
from src.builders.interpartner.response import ResponseBuilder
from src.entities.content import Result

class TestResponseBuilder(unittest.TestCase):

    def test_build_should_return_result_instance_successful_always(self):
    
        
        builder = ResponseBuilder()
        result = builder.build([])
        
        self.assertTrue(result.is_success)
        self.assertIsNone(result.message)
        self.assertIsNone(result.licence)
