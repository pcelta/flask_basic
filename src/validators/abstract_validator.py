import abc

class AbstractValidator(object):

    _missing_field = ""

    @abc.abstractmethod
    def validate(self, action, converted_json):
        pass
        
    def _check(self, converted_json, mandatories_fields):
        for mandatory_field in mandatories_fields :
            if mandatory_field not in converted_json :
                self._missing_field = mandatory_field
                return False
                
        return True

    def get_missing_field(self):
        return self._missing_field
