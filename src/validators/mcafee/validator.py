from src.validators.abstract_validator import AbstractValidator

class Validator(AbstractValidator):
    
    def validate(self, action, order):

        if action == "activate" :

            mandatory_fields = [
                "purchase",
                "partnerId",
                "country",
                "msisdn",
                "language",
                "login",
                "password",
                "email",
                "sku",
            ]

            self.set_mandatory_fields_for_partner(mandatory_fields)
            return self._check(order)

        if action == "cancel" :
            mandatory_fields = [
                "partnerId",
                "msisdn",
                "sku",
                "license",
                "productKey",
                "purchase",
            ]

            self.set_mandatory_fields_for_partner(mandatory_fields)
            return self._check(order)

        return False

