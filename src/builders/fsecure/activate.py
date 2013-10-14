#import ipdb; ipdb.set_trace()
from src.builders.abstract_builder import AbstractBuilder
from src.entities.content import Content

class ActivateBuilder(AbstractBuilder):

    def build(self, order):
        data = {
            "extref"        : order['customerIdentification'],
            "license_size"  : order['license'],
         }

        return Content(data)
