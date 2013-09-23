import abc

class AbstractBuilder(object):

    @abstractmethod
    def build(self, order):
