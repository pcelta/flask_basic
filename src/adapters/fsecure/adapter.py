from src.adapters.abstract_adapter import AbstractAdapter
from src.entities.content import Content


class Adapter(AbstractAdapter):

    def call(self, content):
        if not isinstance(content, Content) :
            raise ValueError('Invalid Argument. Must be Content instance')

