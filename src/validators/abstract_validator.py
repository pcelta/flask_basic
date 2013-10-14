import abc

class AbstractValidator(object):

    _mandatory_fields_for_all = [
        "partner", "callback"
    ]

    _mandatory_fields_for_partner   = []
    _missing_field                  = ""

    @abc.abstractmethod
    def validate(self, action, order):
        pass
        
    def _check(self, order):
        fields = self._mandatory_fields_for_all + self._mandatory_fields_for_partner
        for mandatory_field in fields :
            if mandatory_field not in order :
                self._missing_field = mandatory_field
                return False

        return True

    def get_missing_field(self):
        return self._missing_field

    def set_mandatory_fields_for_partner(self, mandatory_fields):
        self._mandatory_fields_for_partner = mandatory_fields
