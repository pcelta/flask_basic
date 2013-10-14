from src.builders.abstract_builder import AbstractResponseBuilder
from src.entities.content import Result

class Builder(AbstractResponseBuilder):

    _SUCCESS                = 200
    _PARAMETER_ERROR        = 400
    _AUTHENTICATION_FAILED  = 401
    _NO_PERMISSION          = 403
    _NOT_ALLOWED            = 405
    _RESOURCE_ERROR         = 500

    def build(self, response):

        result = Result()
        result.is_success = False

        if response.status_code == self._SUCCESS:
            result.is_success = True

        elif response.status_code == self._PARAMETER_ERROR:
            result.message = "Invalid value for customerIdentification or licence parameter"
        else:
            # add log
            pass

        return result
