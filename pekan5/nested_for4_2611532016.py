tinggi = int(input("Masukkan tinggi pola(bilangan genap, misal 10): "))

if tinggi % 2 != 0:
    print("harus bilangan genap")
else:
    a = tinggi 
    c = a
    lebar = (2 * tinggi) - 1
    
    for i in range(1, tinggi + 1):
        b = c + 1
        
        for j in range(1, lebar + 1):
            if j == 1 or j == tinggi:
                if j == 1 or j == lebar:
                    print("#", end="")
                else:
                    if j == 1 or j == lebar:
                        print("|", end="")
                    else:
                        if j == c:
                            print("<", end="")
                        elif j == b:
                            print(">", end="")
                        elif j == (lebar - c + 1):
                            print("<", end="")
                        elif j > b and j < (lebar - c + 1):
                            print("=", end="")
    print()