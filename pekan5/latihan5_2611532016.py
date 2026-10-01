tinggi_2611532016 = int(input("Masukkan tinggi segitiga: "))

for i in range(1, tinggi_2611532016 + 1):

    for spasi in range(tinggi_2611532016 - i):
        print(" ", end="")

    for bintang in range(i):
        print("*", end=" ")

    print()