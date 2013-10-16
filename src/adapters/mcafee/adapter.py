from src.adapters.abstract_adapter import AbstractAdapter
from src.entities.content import Content
from configs.loader import Loader
import requests


class Adapter(AbstractAdapter):

    def call(self, content):

        if not isinstance(content, Content) :
            raise ValueError('Invalid Argument. Must be Content instance')

        settings = Loader.get_partner_settings('MCAFEE')
        url = settings["url"]
        response = requests.post(url, content.data)

        return self._builder.build(response)
