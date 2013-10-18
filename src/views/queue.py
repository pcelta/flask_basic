
import json

from src.validators.json_validator import JsonValidator
from configs.loader import Loader
import pika


class Queue(object):

    _validator = None
    _JSON_INVALID_REPSONSE = '{"error" : "Invalid JSON"}'
    _MESSAGE_QUEUED_RESPONSE = '{"success" : "true", "message" : "message queued"}'

    def __init__(self, validator):
        if not isinstance(validator, JsonValidator):
            raise ValueError('Invalid Argument. Must be JsonValidator instance')

        self._validator = validator

    def _send(self, queue_name, str_json):

        from src.message_queue.manager import send
        send(queue_name, str_json)

    def activate(self, str_json):
        if (self._validator.validate(str_json)):
            self._send('activate', str_json)
            return self._MESSAGE_QUEUED_RESPONSE

        return self._JSON_INVALID_REPSONSE

    def upgrade(self, str_json):
        if (self._validator.validate(str_json)):
            self._send('upgrade', str_json)
            return self._MESSAGE_QUEUED_RESPONSE

        return self._JSON_INVALID_REPSONSE

    def downgrade(self, str_json):
        if (self._validator.validate(str_json)):
            self._send('downgrade', str_json)
            return self._MESSAGE_QUEUED_RESPONSE

        return self._JSON_INVALID_REPSONSE

    def cancel(self, str_json):
        if (self._validator.validate(str_json)):
            self._send('cancel', str_json)
            return self._MESSAGE_QUEUED_RESPONSE

        return self._JSON_INVALID_REPSONSE

    def reactivate(self, str_json):
        if (self._validator.validate(str_json)):
            self._send('reactivate', str_json)
            return self._MESSAGE_QUEUED_RESPONSE

        return self._JSON_INVALID_REPSONSE
