angka1_2016 = int(input("Input angka-1: "))
angka2_2016 = int(input("Input angka-2: "))

print("\nNilai awal angka1_2016 =", angka1_2016)
print("Nilai angka2_2016 =", angka2_2016)

hasil = angka1_2016
print("\nAssigment biasa (=)")
print("hasil =", hasil)

hasil = angka1_2016
hasil += angka2_2016
print("\nAssigment penambahan (+=)")
print("hasil =", hasil)

hasil = angka1_2016
hasil -= angka2_2016
print("\nAssigment pengurangan (-=)")
print("hasil =", hasil)

hasil = angka1_2016
hasil *= angka2_2016
print("\nAssigment perkalian (*=)")
print("hasil =", hasil)

if angka2_2016 != 0:
    hasil = angka1_2016
    hasil /= angka2_2016
    print("\nAssigment pembagian (/=)")
    print("hasil =", hasil)
    
    hasil = angka1_2016
    hasil //= angka2_2016
    print("\nAssigment pembagian bulat (//=)")
    print("hasil =", hasil)
    
    hasil = angka1_2016
    hasil %= angka2_2016
    print("\nAssigment sisa pembagian (%=)")
    print("hasil =", hasil)
else:
    print("\nPembagian tidak dapat dilakukan")
    print("angka kedua tidak boleh bernilai 0")
 
hasil = angka1_2016
hasil **= angka2_2016
print("\nAssigment pemangkatan (**=)")
print("hasil =", hasil)
