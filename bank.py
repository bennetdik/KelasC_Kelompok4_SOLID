# from datetime import date

# class BankAccount:
#     def __init__(self, pemilik, saldo_awal):
#         self.pemilik = pemilik
#         self.__saldo = saldo_awal
#         self.__log = []  # Log transaksi
#         self.__log.append(
#             f" {date.today()} - Tanggal Pembuatan\n Saldo awal: {saldo_awal}\n"
#             f" {date.today()} - Deposit: {self.format_rupiah(saldo_awal)}, Saldo: {self.format_rupiah(self.__saldo)}\n"
#             f" {date.today()} - Penarikan: {self.format_rupiah(0)}, Saldo: {self.format_rupiah(self.__saldo)}\n"
#             )

#     #mengatur digit sesuai rupiah
#     def format_rupiah(self, jumlah):
#         return f"Rp{jumlah:,.2f}".replace(".", ",").replace(".", ",", 1)
    
#     #menampilkan semua nasabah
#     def tampilkan_nasabah(self):
#         print(f"{'No.':<5} {'Nama':<20} {'Saldo':>50}")
#         print("-" * 75)
#         for i, akun in enumerate(daftar_akun, start=1):
#             print(f"| {i:<5} | {akun.pemilik:<30} | {self.format_rupiah(akun.get_saldo()):>30} |")
#         print("-" * 75)

#     #method untuk menampilkan informasi akun
#     def info_akun(self):
#         print(f"Pemilik Akun: {self.pemilik}")
#         print(f"Saldo Awal  : {self.format_rupiah(self.__saldo)}")
#         # print(f"Log Transaksi: {len(self.__log)} transaksi tercatat.")

#     # Method getter untuk membaca saldo (tanpa bisa diubah langsung)
#     def get_saldo(self):
#         return self.__saldo

#     # Method setter untuk memperbarui saldo dengan validasi
#     def set_saldo(self, jumlah):
#         if jumlah < 0:
#             print("Jumlah saldo tidak boleh negatif!")
#         else:
#             self.__saldo = jumlah
#             print(f"Saldo berhasil diperbarui menjadi: {self.format_rupiah(self.__saldo)}")

#     # Metode untuk menambah saldo
#     def deposit(self, jumlah):
#         if jumlah > 0:
#             self.__saldo += jumlah
#             print(f"Saldo bertambah: {self.format_rupiah(jumlah)}, Saldo sekarang: {self.format_rupiah(self.__saldo)}")
#             self.__log.append(f"[{date.today()}] Deposit: {self.format_rupiah(jumlah)}, Saldo: {self.format_rupiah(self.__saldo)}")
#         else:
#             print("Jumlah deposit harus positif!")

#     # Metode untuk menarik saldo
#     def withdraw(self, jumlah):
#         if jumlah > 0 and jumlah <= self.__saldo:
#             self.__saldo -= jumlah
#             self.__log.append(f"[{date.today()}] Penarikan: {self.format_rupiah(jumlah)}, Saldo: {self.format_rupiah(self.__saldo)}")
#             print(f"Berhasil menarik: {self.format_rupiah(jumlah)}, Saldo sekarang: {self.format_rupiah(self.__saldo)}")
#         else:
#             print("Penarikan gagal: saldo tidak mencukupi atau jumlah tidak valid")

#     # Metode untuk menampilkan log transaksi
#     def tampilkan_log(self):
#         print("\nLog Transaksi:")
#         for entry in self.__log:
#             print(entry)

# daftar_akun = [
#     BankAccount("Anindya Ramadhani",   50000000),
#     BankAccount("Aurhel Alana",   72500000),
#     BankAccount("Cathleen Nixie",  43000000),
#     BankAccount("Fritzy Rosmerian", 98000000),
#     BankAccount("Chelsea Davina",   61000000),
#     BankAccount("Freya Jayawardana",   35000000),
#     BankAccount("Marsha Lenathea",  27500000),
#     BankAccount("Angelina Christy",  80000000),
#     BankAccount("Abigail Rachel",    92000000),
#     BankAccount("Cornelia Vanisha",  45000000),
#     BankAccount("Michelle Alexandra",  67000000),
# ]


# def tambah_akun():
#     nama = input("Masukkan nama nasabah: ")
#     saldo_awal = int(input("Masukkan saldo awal: Rp"))
#     akun_baru = BankAccount(nama, saldo_awal)
#     daftar_akun.append(akun_baru)
#     print("Akun berhasil ditambahkan.\n")

# def menu_utama():
#     while True:
#         print("Menu Bank Account:")
#         print("1. Tambah Akun")
#         print("2. Tampilkan Nasabah")
#         print("3. Detail nasabah")
#         print("4. Keluar")
#         pilihan = input("Masukkan pilihan: ")

#         if pilihan == '1':
#             tambah_akun()
#         elif pilihan == '2':
#             print(f"DAFTAR NASABAR BANK JARWO Tanggal {date.today()}\n")
#             print("-" * 75)
#             print(f"| {'No.':<5} | {'Nama':<30} | {'Saldo':>30} |")
#             print("-" * 75)
#             for i, akun in enumerate(daftar_akun, start=1):
#                 print(f"| {i:<5} | {akun.pemilik:<30} | {akun.format_rupiah(akun.get_saldo()):>30} |")
#             print("-" * 75)
#         elif pilihan == '3':
#                 print("Pilih detail akun:\n")
#                 nama_akun = input("Masukkan nama nasabah: ")
#                 akun_ditemukan = None
#                 for akun in daftar_akun:
#                     if nama_akun.lower() == akun.pemilik.lower():
#                         akun_ditemukan = akun
#                         break
#                 if akun_ditemukan:
#                     while True:
#                         akun_ditemukan.info_akun()
#                         print("1. Tambah Saldo")
#                         print("2. Tarik Saldo")
#                         print("3. Tampilkan Log Transaksi")
#                         print("4. Kembali ke Menu Utama")
#                         sub_pilihan = input("Masukkan pilihan: ")
#                         if sub_pilihan == '1':
#                             jumlah = int(input("Masukkan jumlah deposit: Rp"))
#                             akun_ditemukan.deposit(jumlah)
#                             akun_ditemukan.tampilkan_log()
#                         elif sub_pilihan == '2':
#                             jumlah = int(input("Masukkan jumlah penarikan: Rp"))
#                             akun_ditemukan.withdraw(jumlah)
#                             akun_ditemukan.tampilkan_log()
#                         elif sub_pilihan == '3':
#                             akun_ditemukan.tampilkan_log()
#                         else:
#                             menu_utama()
#                         print("\n")
#                 else:
#                     print("Nasabah tidak ditemukan.\n")
#         elif pilihan == '4':
#             print("Terima kasih telah menggunakan program ini.")
#             break
#         else:
#             print("Pilihan tidak valid. Silakan coba lagi.\n")
# # Contoh Penggunaan
# if __name__ == "__main__":
#     menu_utama()

class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):        
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

s = stack()
input_string = input("Masukkan string: ")
for char in input_string:
    s.push(char)
print(s)
print(s.pop())
print(s.peek())