from src.validators.abstract_validator import AbstractValidator

class Validator(AbstractValidator):
    
    def validate(self, action, order):
        generic_fields = ["partner", "purchase"]
        
        if action == "activate" :
        
            mandatories_fields = generic_fields + [
                "contractId",
                "password",
                "action",
                "customerIdentification",
                "planCode",
                "startDate",
                "endDate",
                "callback"
            ]
            
            return self._check(order, mandatories_fields)

        if action == "cancel" :
            pass
        return False

