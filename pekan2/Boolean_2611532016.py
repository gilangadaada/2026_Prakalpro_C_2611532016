is_lulus = True
is_cumlaude = True

nilai = 85
batas_lulus = 75

status_kelulusaan = nilai >= batas_lulus

print("=== Check Kelulusan ===")
print("nilai:", nilai)
print("apakah lulus?:", status_kelulusaan)
if is_lulus and is_cumlaude:
    print("Selamat, anda lulus dengan predikat cumlaude!")