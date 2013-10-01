from src.adapters.abstract_adapter import AbstractAdapter
from src.entities.content import Content, Result


class Adapter(AbstractAdapter):

    def call(self, content):

        if not isinstance(content, Content) :
            raise ValueError('Invalid Argument. Must be Content instance')

        result = Result()
        result.is_success = True
        result.message = 'MOCKED ADAPTER'

        return result

