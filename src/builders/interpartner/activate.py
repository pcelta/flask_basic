#import ipdb; ipdb.set_trace()
from src.builders.abstract_builder import AbstractBuilder
from src.entities.content import Content

class ActivateBuilder(AbstractBuilder):

    def build(self, order):
        item_data['CodigoContrato']        = order['contractId']
        item_data['Senha']                 = order['password']
        item_data['CodigoPlano']           = order['planCode']
        item_data['CodigoIdentificacao']   = order['customerIdentification']
        item_data['DataInicio']            = order['startDate']
        item_data['DataTermino']           = order['endDate']
        item_data['Status']                = order['action']

        data['Cliente'] = item_data

        return Content(data)
