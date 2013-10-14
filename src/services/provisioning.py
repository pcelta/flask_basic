from src.provisioners.factory_provisioner import FactoryProvisioner
from src.entities.content import Result
from src.builders.response import Response


class Provisioner(object):

    _factory_provisioner = None

    def __init__(self, factory_provisioner):

        if not isinstance(factory_provisioner, FactoryProvisioner):
            raise ValueError("Invalid Argument. Must be FactoryProvisioner instance")

        self._factory_provisioner = factory_provisioner

    def activate(self, orders):
        
        for order in orders['orders'] :

            if not self._partner_key_exists(order) :
                order['result'] = Result.create_with_partner_missing_error('partner')
                continue

            provisioner = self._factory_provisioner.create(order['partner'])
            order['result'] = provisioner.activate(order)

        builder_response = Response()
        return builder_response.build(orders)

    def upgrade(self, orders):
        
        for order in orders['orders'] :

            if not self._partner_key_exists(order) :
                order['result'] = Result.create_with_partner_missing_error('partner')
                continue

            provisioner = self._factory_provisioner.create(order['partner'])
            order['result'] = provisioner.upgrade(order)
        
        builder_response = Response()
        return builder_response.build(orders) 

    def downgrade(self, orders):
        
        for order in orders['orders'] :

            if not self._partner_key_exists(order) :
                order['result'] = Result.create_with_partner_missing_error('partner')
                continue

            provisioner = self._factory_provisioner.create(order['partner'])
            order['result'] = provisioner.downgrade(order)
        
        builder_response = Response()
        return builder_response.build(orders)

    def cancel(self, orders):

        for order in orders['orders'] :

            if not self._partner_key_exists(order) :
                order['result'] = Result.create_with_partner_missing_error('partner')
                continue

            provisioner = self._factory_provisioner.create(order['partner'])
            order['result'] = provisioner.cancel(order)

        builder_response = Response()
        return builder_response.build(orders)

    def _partner_key_exists(self, order):
        if 'partner' not in order :
            return False

        return True



