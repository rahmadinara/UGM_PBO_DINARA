class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

    def keliling(self):
        return 4 * self.sisi

    def tampilkan(self):
        print("Luas: " + str(self.luas()))
        print("Keliling: " + str(self.keliling()))

Persegi1 = Persegi(5)
Persegi1.tampilkan()

