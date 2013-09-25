import abc

class AbstractValidator(object):

    @abc.abstractmethod
    def validate(self, action, converted_json):
        pass
        
    def _check(self, converted_json, mandatories_fields):
        for mandatory_field in mandatories_fields :
            if mandatory_field not in converted_json :
                return False
                
        return True
