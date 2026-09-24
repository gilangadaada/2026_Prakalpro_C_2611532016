umur_2016 = int(input("Masukkan umur Anda = "))
sim = input("Apakah Anda memiliki SIM C? (y/t): ")[0]

if umur_2016 >= 17 and sim == 'y':
    print("Anda sudah dewasa dan boleh mengendarai sepeda motor")
elif umur_2016 >= 17 and sim != 'y':
    print("Anda sudah dewasa tetapi tidak boleh mengendarai sepeda motor")
elif umur_2016 < 17 and sim == 'y':
    print("Anda belum cukup umur punya SIM")
else:
    print("Anda belum cukup umur dan tidak boleh mengendarai sepeda motor")
print("program selesai")