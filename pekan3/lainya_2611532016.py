print("==================================================")
print("1 OPERATOR KEANGGOTAAN")
print("==================================================")

input_data = input("Masukkan beberapa angka, pisahkan dengan koma): ")

data = [int(angka.strip()) for angka in input_data.split(",")]

nilai_dicari = int(input("Masukkan angka yang dicari: "))

hasil = nilai_dicari in data
print("\nOperator keanggotaan IN:")
print(nilai_dicari, "in", data, "=", hasil)

hasil = nilai_dicari not in data
print("\nOperator keanggotaan NOT IN:")
print(nilai_dicari, "not in", data, "=", hasil)

print("==================================================")
print("1 OPERATOR IDENTITAS")
print("==================================================")

objek1 = data

objek2 = objek1

objek3 = data.copy()

print("objek 1 =", objek1)
print("objek 2 =", objek2)
print("objek 3 =", objek3)

hasil = objek1 is objek2
print("\nOperator identitas IS:")
print(objek1, "is", objek2, "=", hasil)

hasil = objek1 is not objek3
print("\nOperator identitas IS NOT:")
print(objek1, "is not", objek3, "=", hasil)

hasil = objek1 is not objek3
print("\nOperator identitas IS NOT:")
print(objek1, "is not", objek3, "=", hasil)

print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =", objek1 is objek3)
print("objek1 == objek3 =", objek1 == objek3)