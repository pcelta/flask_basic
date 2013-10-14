from src.validators.abstract_validator import AbstractValidator

class Validator(AbstractValidator):
    
    def validate(self, action, order):

        if action == "activate" :

            mandatory_fields = [
                "contractId",
                "password",
                "action",
                "customerIdentification",
                "planCode",
                "startDate",
                "endDate",
                "purchase"
            ]

            self.set_mandatory_fields_for_partner(mandatory_fields)
            return self._check(order)

        if action == "cancel" :
            pass
        return False

