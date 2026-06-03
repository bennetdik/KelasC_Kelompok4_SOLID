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
