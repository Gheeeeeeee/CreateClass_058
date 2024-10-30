class persegi_panjang:
    def __init__(self, panjang, lebar) :
        self.panjang = panjang
        self.lebar = lebar

    def hitung_keliling(self):
         return 2 * (self.panjang + self.lebar)
        
    def hitung_luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f"persegi panjang memiliki panjang :{self.panjang} dan lebar {self.lebar} "


pp = persegi_panjang (10,2)
print(pp)
print("Keliling:", pp.hitung_keliling(), "cm")
print("Luas:", pp.hitung_luas(), "cm²")


