from hewan_darat import HewanDarat
from hewan_udara import HewanUdara
from hewan_air import HewanAir
from kandang import Kandang
from kebun_binatang import KebunBinatang
from rawat import RawatKandang


def run():
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


if __name__ == "__main__":
    run()
