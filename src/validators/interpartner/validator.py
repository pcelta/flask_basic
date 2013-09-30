from src.validators.abstract_validator import AbstractValidator

class Validator(AbstractValidator):
    
    def validate(self, action, converted_json):
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
            
            return self._check(converted_json, mandatories_fields)

        if action == "cancel" :
            pass
        return False

