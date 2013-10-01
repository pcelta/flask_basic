class Content(object):

    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        return self._data

class Result(object):

    def __init__(self):
        self._licence    = None
        self._is_success = False
        self._message    = None
        self._json       = None

    @property
    def licence(self):
        return self._licence

    @licence.setter
    def licence(self, licence):
        self._licence = licence

    @property
    def is_success(self):
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        self._is_success = is_success

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message

    @property
    def json(self):
        return self._json

    @json.setter
    def json(self, json):
        self._json = json

    @staticmethod
    def create_with_partner_missing_error():
        result = Result()
        result.is_success = false
        result.message = "partner field missing"

        return result

    @staticmethod
    def create_with_success_default():
        result = Result()
        result.is_success = True

        return result


