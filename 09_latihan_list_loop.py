# Buat program untuk memasukkan nilai ujian lebih dari 1
# Program akan berhenti jika penhgguna memasukkan nilai 0
# Hitung rata-rata nilai ujian
# Jika rata-rata lebih dari 80, tampilkan pesan "Selamat, Anda lulus!"
# Jika rata-rata kurang dari atau sama dengan 80, tampilkan pesan "Maaf, Anda tidak lulus."

nilai_ujian = []
while True:
    nilai = int(input("Masukkan nilai ujian (0 untuk berhenti): "))
    if nilai == 0:
        break
    nilai_ujian.append(nilai)
    if len(nilai_ujian) == 0:
        print("Tidak ada nilai ujian yang dimasukkan.")
    else:
        rata_rata = sum(nilai_ujian) / len(nilai_ujian)
        print(f"Rata-rata nilai ujian: {rata_rata:.2f}")
        if rata_rata > 80:
            print("Selamat, Anda lulus!")
        else:
            print("Maaf, Anda tidak lulus.")