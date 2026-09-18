print("=== SISTEM TRANSAKSI TOKO ===")

nama_2016 = input("Masukkan Nama Pelanggan : ")
status_2016 = input("Masukkan Status Pelanggan (member/nonmember) : ").lower()
total_belanja_2016 = float(input("Masukkan Total Belanja : Rp"))
jumlah_barang_2016 = int(input("Masukkan Jumlah Barang : "))
kode_promo_2016 = input("Masukkan Kode Promo : ").upper()

syarat_belanja_2016 = total_belanja_2016 >= 200000
syarat_barang_2016 = jumlah_barang_2016 >= 3
status_member_2016 = status_2016 == "member"

daftar_promo_2016 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

promo_tersedia_2016 = kode_promo_2016 in daftar_promo_2016
promo_tidak_tersedia_2016 = kode_promo_2016 not in daftar_promo_2016

diskon_member_2016 = status_member_2016 and syarat_belanja_2016

# Memotong baris panjang menggunakan tanda kurung
promo_didapatkan_2016 = promo_tersedia_2016 and (
    syarat_belanja_2016 or syarat_barang_2016
)

bukan_member_2016 = not status_member_2016

if diskon_member_2016:
    persentase_diskon_2016 = 0.10
else:
    persentase_diskon_2016 = 0.05 if syarat_belanja_2016 else 0

besar_diskon_2016 = total_belanja_2016 * persentase_diskon_2016

total_pembayaran_2016 = total_belanja_2016 - besar_diskon_2016

if jumlah_barang_2016 > 0:
    rata_rata_barang_2016 = total_belanja_2016 / jumlah_barang_2016
else:
    rata_rata_barang_2016 = 0

# Memotong baris rumus sisa pembagian
sisa_pembagian_2016 = (
    int(total_belanja_2016) % jumlah_barang_2016 
    if jumlah_barang_2016 > 0 else 0
)


poin_2016 = 0
if status_member_2016:
    poin_2016 += int(total_pembayaran_2016 // 10000)

jumlah_barang_tersisa_2016 = jumlah_barang_2016
if promo_didapatkan_2016:
    jumlah_barang_tersisa_2016 -= 1

kode_1_2016 = ["HEMAT10"]
kode_2_2016 = ["HEMAT10"]

nilai_sama_2016 = kode_1_2016 == kode_2_2016
objek_sama_2016 = kode_1_2016 is kode_2_2016
objek_berbeda_2016 = kode_1_2016 is not kode_2_2016


kode_member_2016 = 1 if status_member_2016 else 0
kode_belanja_2016 = 2 if syarat_belanja_2016 else 0
kode_barang_2016 = 4 if syarat_barang_2016 else 0
bit_promo_2016 = 8 if promo_tersedia_2016 else 0

# Operator OR (|)
kode_status_2016 = (
    kode_member_2016
    | kode_belanja_2016
    | kode_barang_2016
    | bit_promo_2016
)

cek_member_2016 = kode_status_2016 & 1
cek_belanja_2016 = kode_status_2016 & 2
cek_barang_2016 = kode_status_2016 & 4
cek_promo_2016 = kode_status_2016 & 8

kode_referensi_2016 = 11
perbandingan_status_2016 = kode_status_2016 ^ kode_referensi_2016

kode_shift_2016 = kode_status_2016 << 1


member_access_2016 = bool(cek_member_2016)
promo_access_2016 = bool(cek_promo_2016)
free_shipping_access_2016 = syarat_belanja_2016 and syarat_barang_2016


print("\n=== DATA PELANGGAN ===")
print("Nama Pelanggan       :", nama_2016)
print("Status Pelanggan     :", status_2016)
print("Total Belanja        : Rp", total_belanja_2016)
print("Jumlah Barang        :", jumlah_barang_2016)
print("Kode Promo           :", kode_promo_2016)


print("\n=== HASIL VALIDASI ===")
print("Belanja >= Rp200000  :", syarat_belanja_2016)
print("Jumlah Barang >= 3   :", syarat_barang_2016)
print("Status Member        :", status_member_2016)
print("Kode Promo Tersedia  :", promo_tersedia_2016)
print("Mendapatkan Diskon   :", diskon_member_2016)
print("Mendapatkan Promo    :", promo_didapatkan_2016)


print("\n=== HASIL PERHITUNGAN ===")
print("Besarnya Diskon      : Rp", besar_diskon_2016)
print("Total Pembayaran     : Rp", total_pembayaran_2016)
print("Rata-rata Harga      : Rp", rata_rata_barang_2016)
print("Sisa Pembagian       :", sisa_pembagian_2016)


print("\n=== HAK AKSES PELANGGAN ===")
print("Kode Hak Akses       :", format(kode_status_2016, "04b"))
print("Member Access        :", member_access_2016)
print("Promo Access         :", promo_access_2016)
print("Free Shipping Access :", free_shipping_access_2016)
print("Poin Pelanggan       :", poin_2016)


print("\n=== OPERATOR IDENTITAS ===")
print("kode_1 == kode_2     :", nilai_sama_2016)
print("kode_1 is kode_2     :", objek_sama_2016)
print("kode_1 is not kode_2 :", objek_berbeda_2016)


print("\n=== OPERASI BITWISE ===")
print("Kode Status Transaksi")
print("0001 | 0010 | 0100 | 1000")

print("Kode Biner           :", format(kode_status_2016, "04b"))
print("Kode Desimal         :", kode_status_2016)

print("\n=== PEMERIKSAAN STATUS ===")

print("\nCek Member")
print(format(kode_status_2016, "04b"), "& 0001")
print("Hasil Biner         :", format(cek_member_2016, "04b"))
print("Hasil Desimal       :", cek_member_2016)

print("\nCek Belanja")
print(format(kode_status_2016, "04b"), "& 0010")
print("Hasil Biner         :", format(cek_belanja_2016, "04b"))
print("Hasil Desimal       :", cek_belanja_2016)

print("\nCek Jumlah Barang")
print(format(kode_status_2016, "04b"), "& 0100")
print("Hasil Biner         :", format(cek_barang_2016, "04b"))
print("Hasil Desimal       :", cek_barang_2016)

print("\nCek Promo")
print(format(kode_status_2016, "04b"), "& 1000")
print("Hasil Biner         :", format(cek_promo_2016, "04b"))
print("Hasil Desimal       :", cek_promo_2016)

# Memotong baris print panjang pada segmen XOR
print("\n=== PERBANDINGAN STATUS (XOR) ===")
print("Kode Transaksi      :", format(kode_status_2016, "04b"))
print("Kode Referensi      :", format(kode_referensi_2016, "04b"))
print(
    format(kode_status_2016, "04b"), "^", 
    format(kode_referensi_2016, "04b")
)
print("Hasil Biner         :", format(perbandingan_status_2016, "04b"))
print("Hasil Desimal       :", perbandingan_status_2016)

print("\n=== SHIFT ===")
print(format(kode_status_2016, "04b"), "<< 1")
print("Hasil Biner         :", format(kode_shift_2016, "b"))
print("Hasil Desimal       :", kode_shift_2016)

print("\n=== SELESAI ===")
