import abc

class AbstractAdapter(object):
    @abc.abstractmethod
    def call(self, order):
        pass
