class Jurnal(Koleksi):
    def __init__(self, kode, judul, tahun_terbit, penerbit,
                 bidang_studi, impact_factor):

        super().__init__(kode, judul, tahun_terbit, penerbit)

        self.bidang_studi = bidang_studi
        self.impact_factor = impact_factor

    def tampilkan_data(self):
        print(f"Jenis          : Jurnal")
        print(f"Kode Koleksi   : {self.kode}")
        print(f"Judul          : {self.judul}")
        print(f"Tahun Terbit   : {self.tahun_terbit}")
        print(f"Penerbit       : {self.penerbit}")
        print(f"Impact Factor  : {self.impact_factor}")
        print(f"Bidang Studi   : {self.bidang_studi}")