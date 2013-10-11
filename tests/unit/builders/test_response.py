import unittest
from src.builders.response import Response
from src.entities.content import Result

class TestResponse(unittest.TestCase):

    def test_build_should_return_response_successful_with_one_result(self):

        default_result = Result.create_with_success_default()

        orders = {
            "orders" : [
                {
                    "partner"               : "interpartner",
                    "purchase"              : "1", 
                    "contractId"            : "", 
                    "password"              : "xxx", 
                    "action"                : "incluir", 
                    "customerIdentification" : "1", 
                    "planCode"              : "001", 
                    "startDate"             : "", 
                    "endDate"               : "", 
                    "callback"              : "",
                    "result"                : default_result
                }
            ]
        }

        builder = Response()
        result = builder.build(orders)

        expected = {
            "responses" : [
                { "success"   : True, "purchase"  : "1" }
            ]
        }

        self.assertEquals(expected, result)

        def test_build_should_return_response_successful_with_two_result(self):

            default_result = Result.create_with_success_default()

            failed_result = Result()
            orders = {
                "orders" : [
                    {
                        "partner"               : "interpartner",
                        "purchase"              : "1", 
                        "contractId"            : "", 
                        "password"              : "xxx", 
                        "action"                : "incluir", 
                        "customerIdentification" : "1", 
                        "planCode"              : "001", 
                        "startDate"             : "", 
                        "endDate"               : "", 
                        "callback"              : "",
                        "result"                : default_result
                    },
                    {
                        "partner"               : "interpartner",
                        "purchase"              : "2", 
                        "contractId"            : "", 
                        "password"              : "xxx", 
                        "action"                : "incluir", 
                        "customerIdentification" : "2", 
                        "planCode"              : "001", 
                        "startDate"             : "", 
                        "endDate"               : "", 
                        "callback"              : "",
                        "result"                : failed_result
                    }
                ]
            }

            builder = Response()
            result = builder.build(orders)

            expected = {
                "responses" : [
                    { "success"   : True,  "purchase"  : "1" },
                    { "success"   : False, "purchase"  : "2" }
                ]
            }

            self.assertEquals(expected, result)

    def test_build_should_return_response_successful_with_one_result_and_message(self):

        default_result = Result()
        default_result.message = 'provisionig failed'

        orders = {
            "orders" : [
                {
                    "partner"               : "interpartner",
                    "purchase"              : "1", 
                    "contractId"            : "", 
                    "password"              : "xxx", 
                    "action"                : "incluir", 
                    "customerIdentification" : "1", 
                    "planCode"              : "001", 
                    "startDate"             : "", 
                    "endDate"               : "", 
                    "callback"              : "",
                    "result"                : default_result
                }
            ]
        }

        builder = Response()
        result = builder.build(orders)

        expected = {
            "responses" : [
                { "success"   : False, "purchase"  : "1", "message" : "provisionig failed" }
            ]
        }

        self.assertEquals(expected, result)

    def test_build_should_return_response_successful_with_one_result_and_licence(self):

        default_result = Result()
        default_result.licence = 'lklklk'

        orders = {
            "orders" : [
                {
                    "partner"               : "interpartner",
                    "purchase"              : "1", 
                    "contractId"            : "", 
                    "password"              : "xxx", 
                    "action"                : "incluir", 
                    "customerIdentification" : "1", 
                    "planCode"              : "001", 
                    "startDate"             : "", 
                    "endDate"               : "", 
                    "callback"              : "",
                    "result"                : default_result
                }
            ]
        }

        builder = Response()
        result = builder.build(orders)

        expected = {
            "responses" : [
                { "success"   : False, "purchase"  : "1", "licence" : "lklklk" }
            ]
        }

        self.assertEquals(expected, result)

