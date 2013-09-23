from ..validators.order_validator import PartnerOrderValidator

class Provisioner(object):

    def activate(self, json):
        for order in json['orders'] :
            if 'partner' is not order :
                continue

            validator = PartnerOrderValidator(order['partner'])
            if validator.validate(order) :
                self._do_activate(order)

    def _do_activate(self, order):
        pass
