from abc import ABC, abstractmethod

class BaseDAO(ABC):
    @abstractmethod
    def inser(self, entity):
        pass
    @abstractmethod
    def find_all(self):
        pass