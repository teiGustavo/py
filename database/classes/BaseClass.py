import abc


class BaseClass(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def findById(self, id):
        return
