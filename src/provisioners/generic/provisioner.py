from src.provisioners.abstract_provisioner import AbstractProvisioner

from src.entities.content import Result

class Provisioner(AbstractProvisioner):

    def activate(self, order):

        validator = self._factory_validator.create(order['partner'])

        if validator.validate("activate", order) :
            builder = self._factory_builder.create(order['partner'], 'activate')
            adapter = self._factory_adapter.create(order['partner'])
            return adapter.call(builder.build(order))

        return Result.create_with_partner_missing_error(validator.get_missing_field())

    def cancel(self, order):

        validator = self._factory_validator.create(order['partner'])

        if validator.validate("cancel", order) :
            builder = self._factory_builder.create(order['partner'], 'cancel')
            adapter = self._factory_adapter.create(order['partner'])
            return adapter.call(builder.build(order))

        return Result.create_with_partner_missing_error(validator.get_missing_field())

    def upgrade(self, order):

        validator = self._factory_validator.create(order['partner'])

        if validator.validate("upgrade", order) :
            builder = self._factory_builder.create(order['partner'], 'upgrade')
            adapter = self._factory_adapter.create(order['partner'])
            return adapter.call(builder.build(order))

        return Result.create_with_partner_missing_error(validator.get_missing_field())

    def downgrade(self, order):

        validator = self._factory_validator.create(order['partner'])

        if validator.validate("downgrade", order) :
            builder = self._factory_builder.create(order['partner'], 'downgrade')
            adapter = self._factory_adapter.create(order['partner'])
            return adapter.call(builder.build(order))

        return Result.create_with_partner_missing_error(validator.get_missing_field())

    def reactivate(self, order):

        validator = self._factory_validator.create(order['partner'])

        if validator.validate("reactivate", order) :
            builder = self._factory_builder.create(order['partner'], 'reactivate')
            adapter = self._factory_adapter.create(order['partner'])
            return adapter.call(builder.build(order))

        return Result.create_with_partner_missing_error(validator.get_missing_field())

