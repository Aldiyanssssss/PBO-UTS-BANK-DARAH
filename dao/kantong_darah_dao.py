from abc import ABC, abstractmethod

class KantongDarahDAO(ABC):
    @abstractmethod
    def insert(self, entity): pass
    @abstractmethod
    def update_status(self, kode_kantong, status): pass
    @abstractmethod
    def delete(self, kode_kantong): pass
    @abstractmethod
    def find_all(self): pass
    @abstractmethod
    def find_available(self, gol_darah, rhesus, jumlah): pass
    @abstractmethod
    def hitung_stok_by_goldar(self): pass
