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

class HewanBerenang(ABC):
    @abstractmethod
    def berenang(self):
        pass

class kandang:
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan: Hewan):
        self.hewan_list.append(hewan)

    def tampilkan_hewan(self):
        for hewan in self.hewan_list:
            hewan.nama_hewan()

class rawat_kandang:
    
    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")

class KebunBinatang:
    def __init__(self, kandang: kandang):
        self.kandang = kandang

    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:

            print(f"Sedang merawat {hewan.nama}")

            if hasattr(hewan, "makan"):
                hewan.makan()

            if isinstance(hewan, HewanBerjalan):
                hewan.berjalan()

            if isinstance(hewan, HewanTerbang):
                hewan.terbang()

            if isinstance(hewan, HewanBerenang):
                hewan.berenang()

            print()