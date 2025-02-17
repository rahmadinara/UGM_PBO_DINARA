class Buah:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def tampilkan(self):
        print("Buah: " + self.nama)
        print("Harga: " + str(self.harga))

Buah1 = Buah("Mangga", 10000)
Buah1.tampilkan()
