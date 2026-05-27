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

class HewanDarat(Hewan, HewanBerjalan):
    def berjalan(self):
        print(f"{self.nama} berjalan.")

class HewanUdara(Hewan, HewanTerbang):
    def terbang(self):
        print(f"{self.nama} terbang.")

class HewanAir(Hewan, HewanBerenang):
    def berenang(self):
        print(f"{self.nama} berenang.")

class kandang:
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan: Hewan):
        self.hewan_list.append(hewan)

    def tampilkan_hewan(self):
        for hewan in self.hewan_list:
            hewan.nama_hewan()

class RawatKandang:
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

class Burung(Hewan, HewanTerbang):
    def makan(self):
        print(f"{self.nama} sedang makan")
    def terbang(self):
        print(f"{self.nama} sedang terbang")

class Kucing(Hewan, HewanBerjalan):
    def makan(self):
        print(f"{self.nama} sedang makan")
    def berjalan(self):
        print(f"{self.nama} sedang berjalan")

class Ikan(Hewan, HewanBerenang):
    def makan(self):
        print(f"{self.nama} sedang makan")
    def berenang(self):
        print(f"{self.nama} sedang berenang")

if __name__ == "__main__":
    k = kandang()
    zoo = KebunBinatang(k)

    while True:
        print("=== MENU ===")
        print("1. Tambah Burung")
        print("2. Tambah Kucing")
        print("3. Tambah Ikan")
        print("4. Tampilkan Daftar Hewan")
        print("5. Rawat Semua Hewan")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Masukkan nama burung: ")
            burung = Burung(nama)
            k.tambah_hewan(burung)
            print(f"{nama} berhasil ditambahkan!")

        elif pilihan == "2":
            nama = input("Masukkan nama kucing: ")
            kucing = Kucing(nama)
            k.tambah_hewan(kucing)
            print(f"{nama} berhasil ditambahkan!")

        elif pilihan == "3":
            nama = input("Masukkan nama ikan: ")
            ikan = Ikan(nama)
            k.tambah_hewan(ikan)
            print(f"{nama} berhasil ditambahkan!")

        elif pilihan == "4":
            print("=== DAFTAR HEWAN ===")
            k.tampilkan_hewan()

        elif pilihan == "5":
            print("=== MERAWAT HEWAN ===")
            zoo.rawat_semua_hewan()

        elif pilihan == "6":
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid, coba lagi")
