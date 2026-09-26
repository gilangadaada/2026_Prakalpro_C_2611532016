print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# 1. INPUT DATA PENGUNJUNG

nama_pengunjung_2016 = input("Masukkan Nama Pengunjung        : ")
umur_2016 = int(input("Input umur anda                 : "))
sim_2016 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()
jumlah_tiket_2016 = int(input("Masukkan jumlah tiket           : "))

# Validasi jumlah tiket menggunakan if tunggal
if jumlah_tiket_2016 <= 0:
    print("Peringatan: Kuota tiket tidak valid!")


# 2. PEMILIHAN PAKET WAHANA MENGGUNAKAN MATCH-CASE

print("\nPilihan Paket Wahana (1-5):")
print(" 1. Safari Rimba         (Rp 50,000)")
print(" 2. Arung Jeram          (Rp 75,000)")
print(" 3. Motor ATV Ekstrim    (Rp 120,000)")
print(" 4. Roller Coaster Kilat (Rp 100,000)")
print(" 5. All-Access VIP       (Rp 220,000)")

paket_2016 = int(input("Masukkan nomor paket (1-5) : "))

match paket_2016:
    case 1:
        nama_wahana_2016 = "Wahana Safari Rimba"
        harga_satuan_2016 = 50000

    case 2:
        nama_wahana_2016 = "Wahana Arung Jeram"
        harga_satuan_2016 = 75000

    case 3:
        nama_wahana_2016 = "Wahana Motor ATV Ekstrim"
        harga_satuan_2016 = 120000

    case 4:
        nama_wahana_2016 = "Wahana Roller Coaster Kilat"
        harga_satuan_2016 = 100000

    case 5:
        nama_wahana_2016 = "Wahana All-Access VIP"
        harga_satuan_2016 = 220000

    case _:
        print("Paket wahana tidak valid!")
        raise SystemExit


# 3. VALIDASI IZIN KENDALI WAHANA
#    Menggunakan if-elif-else dan operator logika

print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

if paket_2016 == 3 and umur_2016 >= 17 and sim_2016 == 'y':
    status_akses_2016 = (
        "Anda sudah dewasa dan boleh mengendarai ATV sendiri."
    )

elif paket_2016 == 3 and umur_2016 >= 17 and sim_2016 != 'y':
    status_akses_2016 = (
        "Anda sudah dewasa tetapi tidak boleh bawa motor ATV "
        "(wajib didampingi instruktur)."
    )

elif paket_2016 == 3 and umur_2016 < 17 and sim_2016 == 'y':
    status_akses_2016 = (
        "Identitas tidak valid: Belum cukup umur memiliki SIM."
    )

elif paket_2016 == 3:
    status_akses_2016 = (
        "Anda belum cukup umur dan tidak boleh bawa motor ATV."
    )

elif umur_2016 >= 10:
    status_akses_2016 = (
        "Anda memenuhi syarat umur untuk wahana ini."
    )

else:
    status_akses_2016 = (
        "Anda belum cukup umur untuk wahana ini."
    )

print(f"Status Akses: {status_akses_2016}")


# 4. INPUT DATA DISKON

is_member_2016 = input("Apakah Anda member? (y/t)       : ").strip().lower()
kode_promo_valid_2016 = input(
    "Apakah kode promo valid? (y/t) : "
).strip().lower()


# 5. PERHITUNGAN SUBTOTAL

subtotal_2016 = harga_satuan_2016 * jumlah_tiket_2016


# 6. MULTI-IF UNTUK DISKON AKUMULATIF

total_diskon_persen_2016 = 0

# Diskon Belanja Besar
if subtotal_2016 >= 200000:
    total_diskon_persen_2016 += 10

# Diskon Member
if is_member_2016 in ['y', 'ya']:
    total_diskon_persen_2016 += 5

# Diskon Voucher Promo
if kode_promo_valid_2016 in ['y', 'ya']:
    total_diskon_persen_2016 += 15

# Diskon Tambahan Rombongan
if jumlah_tiket_2016 >= 5:
    total_diskon_persen_2016 += 5


# 7. PERHITUNGAN NOMINAL DISKON DAN TOTAL BAYAR

nominal_diskon_2016 = (
    subtotal_2016 * (total_diskon_persen_2016 / 100)
)

total_bayar_2016 = subtotal_2016 - nominal_diskon_2016


# 8. EVALUASI KELULUSAN AUDIT

if total_bayar_2016 > 300000:
    catatan_layanan_2016 = (
        "Selamat! Anda berhak mendapatkan Souvenir Gratis."
    )
else:
    catatan_layanan_2016 = (
        "Terima kasih telah berkunjung."
    )


# 9. RINCIAN PEMBAYARAN

print("\n--- Rincian Pembayaran ---")
print(f"Nama Pengunjung  : {nama_pengunjung_2016}")
print(f"Wahana           : {nama_wahana_2016}")
print(f"Harga Satuan     : Rp {harga_satuan_2016:,.0f}")
print(f"Jumlah Tiket     : {jumlah_tiket_2016}")
print(f"Subtotal Belanja : Rp {subtotal_2016:,.0f}")
print(
    f"Total Diskon     : {total_diskon_persen_2016}% "
    f"(Rp {nominal_diskon_2016:,.0f})"
)
print(f"Total Bayar      : Rp {total_bayar_2016:,.0f}")
print(f"Catatan Layanan  : {catatan_layanan_2016}")

print("\nProgram Selesai")