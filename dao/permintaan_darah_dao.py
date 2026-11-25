from abc import ABC, abstractmethod

class PermintaanDarahDAO(ABC):
    @abstractmethod
    def insert(self, entity): pass
    @abstractmethod
    def update_status(self, id_permintaan, status, catatan=None): pass
    @abstractmethod
    def find_all(self): pass
