import abc

class AbstractBuilder(object):

    @abc.abstractmethod
    def build(self, order):
        pass
