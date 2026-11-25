from abc import ABC, abstractmethod

class PendonorDAO(ABC):
    @abstractmethod
    def insert(self, pendonor): pass
    @abstractmethod
    def update(self, pendonor): pass
    @abstractmethod
    def delete(self, id_pendonor): pass
    @abstractmethod
    def find_by_id(self, id_pendonor): pass
    @abstractmethod
    def find_all(self): pass
