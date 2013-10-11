import json

class JsonValidator(object):

    def validate(self, string_json):
        try :
            obj = json.loads(string_json)
        except(ValueError) :
            return False
            
        if 'orders' not in obj.keys() :
            return False

        if type(obj['orders']) is not list :
            return False

        return True




