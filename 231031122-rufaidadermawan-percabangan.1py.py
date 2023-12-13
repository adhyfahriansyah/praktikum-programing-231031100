# Mengambil input nilai dari pengguna
nilai = int(input("Masukkan nilai (0 hingga 100): "))
batas_lulus = 65  # Batas nilai kelulusan

# Memeriksa apakah nilai lebih besar dari batas_lulus
if nilai >= batas_lulus:
    print('Selamat, Anda lulus!')
else:
    print('sayang sekali, Anda tidak lulus')

