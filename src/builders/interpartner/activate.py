#import ipdb; ipdb.set_trace()
from src.builders.abstract_builder import AbstractBuilder
from src.entities.content import Content

class Builder(AbstractBuilder):

    def build(self, order):
        item_data = {
            "CodigoContrato"        : order['contractId'],
            "Senha"                 : order['password'],
            "CodigoPlano"           : order['planCode'],
            "CodigoIdentificacao"   : order['customerIdentification'],
            "DataInicio"            : order['startDate'],
            "DataTermino"           : order['endDate'],
            "Status"                : order['action']
         }

        data = { "Cliente" : item_data}

        return Content(data)
