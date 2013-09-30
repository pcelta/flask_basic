from src.adapters.abstract_adapter import AbstractAdapter
import suds

class Adapter(AbstractAdapter):

    def call(self, content):
        if content not isinstance Content :
            raise ValueError('Invalid Argument. Must be Content instance')

        client = suds.client.Client(self._partner_settings['wsdl'])
        client.service.Incluir()
