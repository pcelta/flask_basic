import abc

class AbstractBuilder(object):

    @abc.abstractmethod
    def build(self, order):
        pass

class AbstractResponseBuilder(object):

    @abc.abstractmethod
    def build(self, response):
        pass
