from src.builders.abstract_builder import AbstractBuilder
from src.entities.content import Content

class Builder(AbstractBuilder):

    def build(self, order):
        data = {
            "extref"        : order['customerIdentification'],
            "license_size"  : order['license'],
         }

        return Content(data)
