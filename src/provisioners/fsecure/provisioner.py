from src.provisioners.abstract_provisioner import AbstractProvisioner

from src.entities.content import Result

class Provisioner(AbstractProvisioner):

    def activate(self, order):

        validator = self._factory_validator.create(order['partner'])

        if validator.validate("activate", order) :
            builder = self._factory_builder.create(order['partner'], 'activate')
            adapter = self._factory_adapter.create(order['partner'])
            adapter.set_action("activate")
            adapter.set_account(order["account"])

            return adapter.call(builder.build(order))

        return Result.create_with_partner_missing_error(validator.get_missing_field())

    def upgrade(self, order):

        validator = self._factory_validator.create(order['partner'])

        if validator.validate("upgrade", order) :
            builder = self._factory_builder.create(order['partner'], 'upgrade')
            adapter = self._factory_adapter.create(order['partner'])
            adapter.set_action("upgrade")
            adapter.set_account(order["account"])

            return adapter.call(builder.build(order))

        return Result.create_with_partner_missing_error(validator.get_missing_field())

    def downgrade(self, order):

        validator = self._factory_validator.create(order['partner'])

        if validator.validate("downgrade", order) :
            builder = self._factory_builder.create(order['partner'], 'downgrade')
            adapter = self._factory_adapter.create(order['partner'])
            adapter.set_action("downgrade")
            adapter.set_account(order["account"])

            return adapter.call(builder.build(order))

        return Result.create_with_partner_missing_error(validator.get_missing_field())          




