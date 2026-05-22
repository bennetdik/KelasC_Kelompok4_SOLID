from abc import ABC, abstractmethod
class Hewan(ABC):
    def __init__(self, nama):
        self.nama = nama

    def nama_hewan(self):
        print(f"Nama hewan: {self.nama}")

class HewanBerjalan(ABC):
    @abstractmethod
    def berjalan(self):
        pass

class HewanTerbang(ABC):
    @abstractmethod
    def terbang(self):
        pass

class kandang:
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)
class rawat_kandang:
    
    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")

class kebun_binatang:
    def __init__(self):
        self.kandang = kandang()

    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            hewan.makan()