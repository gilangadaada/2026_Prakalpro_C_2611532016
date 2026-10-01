ulang_2016 = int(input("Masukkan jumlah perulangan: "))

jumlah = 0
for i in range(1, ulang_2016 + 1):
    print(i, end=" ")
    jumlah = jumlah + i
    
    if i == ulang_2016:
        print(" + ", end="")
    else:
        print(" = ", jumlah, end="")
print()
print("jumlah =", jumlah)