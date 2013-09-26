from src.validators.abstract_validator import AbstractValidator

class Validator(AbstractValidator):
    
    def validate(self, action, converted_json):
        generic_fields = []   
        if action == "activate" :
            mandatories_fields = generic_fields + [
                "purchase", 
                "contractId", 
                "password", 
                "action", 
                "customerIdentification"
            ]
            
            return super(Validator, self)._check(converted_json, mandatories_fields)
            
        return False

