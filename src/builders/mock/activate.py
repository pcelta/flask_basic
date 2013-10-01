from src.builders.abstract_builder import AbstractBuilder
from src.entities.content import Content

class ActivateBuilder(AbstractBuilder):

    def build(self, order):
        data = {}

        return Content(data)
