from hewan import HewanBerjalan, HewanTerbang, HewanBerenang
from kandang import Kandang


class KebunBinatang:
    def _init_(self, kandang: Kandang):
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