from abc import ABC, abstractmethod

class TransaksiDarahDAO(ABC):
    @abstractmethod
    def proses_pengeluaran(self, id_petugas, id_permintaan): pass
    @abstractmethod
    def find_all(self): pass
