class OrderValidator (object):

    def validate(self, order, mandatories_fields):
        for mandatory_field in mandatories_fields :
            if mandatory_field not in order :
                return False
                
        return True

        
        
class PartnerOrderValidator(object):

    partner_name = ""

    def __init__(self, partner_name):
        self.partner_name = partner_name

    def validate(self, order):
        generic_fields = ["purchase", "contractId", "password", "action", "customerIdentification"]

        validator = OrderValidator()

        if self.partner_name.upper() == "INTERPARTNER" :
            interpartner_fields = ["startDate"]
            return validator.validate(order, generic_fields + interpartner_fields)

        return validator.validate(order, generic_fields)
