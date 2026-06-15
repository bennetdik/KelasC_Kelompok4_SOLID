from koleksi_perpustakaan import KoleksiPerpustakaan

class Majalah(KoleksiPerpustakaan):
    def __init__(self, kode, judul, tahun, penerbit, edisi):
        super().__init__(kode, judul, tahun, penerbit)
        self.edisi = edisi

    def tampilkan_detail(self, nomor):
        print(f"Koleksi Nomor {nomor} :")
        print(f"Jenis         : Majalah")
        print(f"Kode Koleksi  : {self.kode_koleksi}")
        print(f"Judul         : {self.judul}")
        print(f"Tahun Terbit  : {self.tahun_terbit}")
        print(f"Penerbit      : {self.penerbit}")
        print(f"Edisi         : {self.edisi}")
        