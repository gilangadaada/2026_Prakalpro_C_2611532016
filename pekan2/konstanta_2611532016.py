from typing import Final
PI : Final = 3.14
print("pi: %f" % (PI))
jari_2016 = float(input("Masukkan nilai jari-jari: "))
luas_2016 = PI * jari_2016 * jari_2016
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_2016, luas_2016))