class Response(object):

    @staticmethod
    def build(orders):
        responses = { "responses" : []}
        for order in orders['orders']:
            result = {
                "success"   : order['result'].is_success
            }
            if "purchase" in order:
                result["purchase"] = order['purchase']

            if order['result'].message != None :
                result['message'] = order['result'].message

            if order['result'].licence != None :
                result['licence'] = order['result'].licence

            responses['responses'].append(result)

        return responses
