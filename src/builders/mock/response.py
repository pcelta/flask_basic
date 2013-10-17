from src.builders.abstract_builder import AbstractResponseBuilder
from src.entities.content import Result

class Builder(AbstractResponseBuilder):

    def build(self, response):
        result = Result.create_with_success_default()
        result.message = 'MOCKED ADAPTER'

        return result
