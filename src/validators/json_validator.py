import json

class RequestValidator(object):

    def validate(self, string_json):
        obj = json.loads(string_json)
        if ('orders' not in obj.keys()) :
            return False

        if (type(obj['orders']) is not list) :
            return False

        return True




