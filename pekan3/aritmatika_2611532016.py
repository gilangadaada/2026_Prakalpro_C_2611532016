angka1_2016 = int(input("Input angka-1: "))
angka2_2016 = int(input("Input angka-2: "))

# penjumlahan
hasil = angka1_2016 + angka2_2016
print("\nOperator Penjumlahan:", hasil)
print("hasil =", hasil)

# pengurangan
hasil = angka1_2016 - angka2_2016
print("\nOperator Pengurangan:", hasil)
print("hasil =", hasil)

hasil = angka1_2016 * angka2_2016
print("\nOperator Perkalian:", hasil)
print("hasil =", hasil)


if angka2_2016 != 0:
    hasil = angka1_2016 / angka2_2016
    print("\nOperator Pembagian:", hasil)
    print("hasil =", hasil)
    
    hasil = angka1_2016 // angka2_2016
    print("\nOperator Pembagian Bulat:", hasil)
    print("hasil =", hasil)
    
    hasil = angka1_2016 % angka2_2016
    print("\nOperator Sisa Pembagian:", hasil)
    print("hasil =", hasil)
else:
    print("angka kedua tidak boleh bernilai 0")
    
    
hasil = angka1_2016 ** angka2_2016
print("\nOperator Pangkat:", hasil)
print("hasil =", hasil)