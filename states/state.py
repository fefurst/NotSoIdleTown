import abc

class State(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def receive(self, bot, message):
        pass

    @abc.abstractmethod
    def act(self, bot):
        pass
