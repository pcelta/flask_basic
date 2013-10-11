import abc

class AbstractValidator(object):

    _missing_field = ""

    @abc.abstractmethod
    def validate(self, action, order):
        pass
        
    def _check(self, order, mandatories_fields):
        for mandatory_field in mandatories_fields :
            if mandatory_field not in order :
                self._missing_field = mandatory_field
                return False
                
        return True

    def get_missing_field(self):
        return self._missing_field
