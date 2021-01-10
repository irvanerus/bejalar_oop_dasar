#materi encapsulation
from geometri.bangun_ruang import BangunRuang
from geometri.persegi_panjang import PersegiPanjang
from geometri.segitiga import segitiga

print("bejalar oop dasar")
p1 = PersegiPanjang(10, 3)
print(p1.info())
print(p1.hitung_luas())

s1 = segitiga(20, 4)
print(s1.info())
print(s1.hitung_luas())

#materi pewarisan
print("\nmencoba membuat object dari kelas bangun ruang")
b1 = BangunRuang()
print(b1.info())
print(b1.hitung_luas())
# belajar polymorphism
print("\npolymorphism")
daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)
for bangun_ruang in daftar_bangun_ruang:
    print(bangun_ruang.info())