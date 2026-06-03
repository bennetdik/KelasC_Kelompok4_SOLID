from abc import ABC, abstractmethod


class Hewan(ABC):
    def __init__(self, nama: str):
        self.nama = nama

    def nama_hewan(self):
        print(f"Nama hewan: {self.nama}")


class HewanBerjalan(ABC):
    @abstractmethod
    def berjalan(self):
        raise NotImplementedError()


class HewanTerbang(ABC):
    @abstractmethod
    def terbang(self):
        raise NotImplementedError()


class HewanBerenang(ABC):
    @abstractmethod
    def berenang(self):
        raise NotImplementedError()

class HewanDarat(Hewan, HewanBerjalan):
    def berjalan(self):
        print(f"{self.nama} berjalan.")

        from hewan import Hewan, HewanTerbang

class HewanUdara(Hewan, HewanTerbang):
    def terbang(self):
        print(f"{self.nama} terbang.")

        from hewan import Hewan, HewanBerenang

class HewanAir(Hewan, HewanBerenang):
    def berenang(self):
        print(f"{self.nama} berenang.")

