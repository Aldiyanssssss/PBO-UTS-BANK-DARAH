from abc import ABC, abstractmethod

class DonorDAO(ABC):
    @abstractmethod
    def insert(self, donor): pass
    @abstractmethod
    def update_verifikasi(self, id_donor, status, catatan=""): pass
    @abstractmethod
    def find_all(self): pass
    @abstractmethod
    def find_by_id(self, id_donor): pass
