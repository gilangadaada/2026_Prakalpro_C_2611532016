
tinggi_2016 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_2016 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a = tinggi_2016
    c = a
    lebar = (2 * tinggi_2016) - 2

    for i in range(1, tinggi_2016 + 1):
        b = c + 1

        for j in range(1, lebar + 1):

            # Baris atas dan bawah
            if i == 1 or i == tinggi_2016:
                if j == 1 or j == lebar:
                    print("#", end="")
                else:
                    print("=", end="")

            # Baris isi
            else:
                if j == 1 or j == lebar:
                    print("|", end="")
                else:
                    if j == c:
                        print("<", end="")
                    elif j == b:
                        print(">", end="")
                    elif j == (lebar - c):
                        print("<", end="")
                    elif j == (lebar - c + 1):
                        print(">", end="")
                    elif j > b and j < (lebar - c):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        # Logika asli Java
        a -= 2

        if a <= 0:
            c = (-a) + 2
        else:
            c = a