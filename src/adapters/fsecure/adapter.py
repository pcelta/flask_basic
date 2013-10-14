from src.adapters.abstract_adapter import AbstractAdapter
from src.entities.content import Content
from configs.loader import Loader
import requests


class Adapter(AbstractAdapter):

    _action     = None
    _account    = None

    def set_action(self, action):
        self._action = action

    def set_account(self, account):
        self._account = account

    def call(self, content):

        if not isinstance(content, Content) :
            raise ValueError('Invalid Argument. Must be Content instance')

        settings = Loader.get_partner_settings('FSECURE')
        authentication_data = settings["authentication"][self._account]
        endpoint = settings["endpoint_%s" % self._action]
        url = settings["url"] % self._account
        response = requests.post(url + endpoint, data=content.data, auth=(authentication_data["user"], authentication_data["password"]))

        return self._builder.build(response)
