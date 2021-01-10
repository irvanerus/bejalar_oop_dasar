class PersegiPanjang():
    def __init__(self, p, l):
        self.p = p
        self.l = l


    def info(self):
        return f"rumus menghitung persegi panjang dengan panjang {self.p} dan lebar {self.p}"

    def hitung_luas(self):
        return self.p * self.l

