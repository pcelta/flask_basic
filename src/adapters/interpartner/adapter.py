from src.adapters.abstract_adapter import AbstractAdapter
from src.entities.content import Content
import suds

class Adapter(AbstractAdapter):

    def call(self, content):
        if not isinstance(content, Content) :
            raise ValueError('Invalid Argument. Must be Content instance')

        client = suds.client.Client(self._partner_settings['wsdl'])
        client.service.Incluir()
