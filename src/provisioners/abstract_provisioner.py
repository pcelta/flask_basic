from src.builders.factory_builder import FactoryBuilder
from src.adapters.factory_adapter import FactoryAdapter
from src.validators.factory_validator import FactoryValidator
import abc

class AbstractProvisioner(object):

    _factory_builder    = None
    _factory_adapter    = None
    _factory_validator  = None

    def __init__(self, factory_builder, factory_adapter, factory_validator):

        if not isinstance(factory_builder, FactoryBuilder):
            raise ValueError("Invalid Argument. Must be FactoryBuilder instance")

        if not isinstance(factory_adapter, FactoryAdapter):
            raise ValueError("Invalid Argument. Must be FactoryAdapter instance")

        if not isinstance(factory_validator, FactoryValidator):
            raise ValueError("Invalid Argument. Must be FactoryValidator instance")

        self._factory_builder = factory_builder
        self._factory_adapter = factory_adapter
        self._factory_validator = factory_validator

    @abc.abstractmethod
    def activate(self, order):
        pass

    @abc.abstractmethod
    def cancel(self, order):
        pass

    @abc.abstractmethod
    def upgrade(self, order):
        pass

    @abc.abstractmethod
    def downgrade(self, order):
        pass

    @abc.abstractmethod
    def reactivate(self, order):
        pass