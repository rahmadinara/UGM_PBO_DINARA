class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def tampilkan(self):
        print('Nama: ' + self.nama)
        print('Umur: ' + str(self.umur))

Budi = Manusia('Budiyono', 40)
Budi.tampilkan()

