from typing import List
from hewan import Hewan

class Kandang:
    def __init__(self):
        self.hewan_list: List[Hewan] = []

    def tambah_hewan(self, hewan: Hewan):
        self.hewan_list.append(hewan)

    def tampilkan_hewan(self):
        if not self.hewan_list:
            print("Belum ada hewan di kandang.")
            return
        for i, hewan in enumerate(self.hewan_list, start=1):
            jenis = type(hewan).__name__
            print(f"{i}. {hewan.nama} ({jenis})")