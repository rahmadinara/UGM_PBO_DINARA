class Mahasiswa:
	def __init__ (self, Nama, NIM, Angkatan):
		self.Nama = Nama
		self.NIM = NIM
		self.Angkatan = Angkatan
	def tampilkan_data(self):
		print("Nama : " + self.Nama)
		print("NIM : " + str(self.NIM))
		print("Angkatan : " + str(self.Angkatan))
      
Mahasiswa1 = Mahasiswa("Andi", 802754, 2022)
Mahasiswa1.tampilkan_data()
