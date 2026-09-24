total_belanja = float(input("Masukkan total belanja (Rp)= "))

input_member = input("Apakah Anda member? (y/t): ").strip().lower()
is_member = input_member in ['y', 'ya']

input_promo = input("apakah promo valid? (y/t): ").strip().lower()
kode_promo_valid = input_promo in ['y', 'ya']

total_diskon_persen = 0

if total_belanja > 1000000:
    total_diskon_persen += 10
    
if is_member:
    total_diskon_persen += 5
    
if kode_promo_valid:
    total_diskon_persen += 15
    
nominal_diskon = total_belanja * (total_diskon_persen / 100)
total_bayar = total_belanja - nominal_diskon

print("\n------ Rincian Pembayaran ---")
print(f"Total Diskon : {total_diskon_persen}% (Rp {nominal_diskon:,.0f})")
print(f"Total Bayar  : Rp {total_bayar:,.0f}")

print(f"total diskon yang anda dapatkan: {total_diskon_persen}")
