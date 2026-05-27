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

class Kandang:
    def __init__(self):
        self.hewan_list = []
    def tambah_hewan(self, hewan: Hewan):
        self.hewan_list.append(hewan)
    def tampilkan_hewan(self):
        if not self.hewan_list:
            print("Belum ada hewan di kandang.")
            return
        for i, hewan in enumerate(self.hewan_list, start=1):
            jenis = type(hewan).__name__
            print(f"{i}. {hewan.nama} ({jenis})")

class RawatKandang:
    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")

class KebunBinatang:
    def __init__(self, kandang: Kandang):
        self.kandang = kandang
    def rawat_semua_hewan(self):
        if not self.kandang.hewan_list:
            print("Belum ada hewan untuk dirawat.")
            return
        for hewan in self.kandang.hewan_list:
            print(f"Sedang merawat {hewan.nama}")
            if isinstance(hewan, HewanBerjalan):
                hewan.berjalan()
            if isinstance(hewan, HewanTerbang):
                hewan.terbang()
            if isinstance(hewan, HewanBerenang):
                hewan.berenang()

k = Kandang()
zoo = KebunBinatang(k)
perawat = RawatKandang()


while True:
    print("\n=== MENU ===")
    print("1. Tambahkan Hewan")
    print("2. Tampilkan Daftar Hewan")
    print("3. Bersihkan Kandang")
    print("4. Rawat Semua Hewan")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Masukkan nama hewan: ")
        print("Pilih jenis hewan:")
        print("1. Hewan Darat")
        print("2. Hewan Udara")
        print("3. Hewan Air")
        jenis = input("Pilih jenis: ")

        if jenis == "1":
            hewan = HewanDarat(nama)
        elif jenis == "2":
            hewan = HewanUdara(nama)
        elif jenis == "3":
            hewan = HewanAir(nama)
        else:
            print("Jenis tidak valid, hewan tidak ditambahkan.")
            continue

        k.tambah_hewan(hewan)  
        print(f"{nama} berhasil ditambahkan!")

    elif pilihan == "2":
        print("=== DAFTAR HEWAN ===")
        k.tampilkan_hewan()  

    elif pilihan == "3":
        print("=== MEMBERSIHKAN KANDANG ===")
        perawat.bersihkan_kandang()

    elif pilihan == "4":
        print("=== MERAWAT HEWAN ===")
        zoo.rawat_semua_hewan()

    elif pilihan == "5":
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")
