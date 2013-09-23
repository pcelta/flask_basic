class FactoryBuilder(object):
    
    @staticmethod
    def create(partner_name):
        if partner_name.upper() == "INTERPARTNER":
            return InterPartner()
