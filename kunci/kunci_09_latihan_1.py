nilai_ujian = [] # List untuk menyimpan nilai ujian
# Loop untuk memasukkan nilai ujian
while True:
    nilai = int(input("Masukkan nilai ujian (0 untuk berhenti): "))
    # Jika nilai yang dimasukkan adalah 0, keluar dari loop
    if nilai == 0:
        break
    # Memasukkan nilai ke dalam list
    nilai_ujian.append(nilai)
    if len(nilai_ujian) == 0: # Jika tidak ada nilai ujian yang dimasukkan
        print("Tidak ada nilai ujian yang dimasukkan.")
    else: # Menghitung rata-rata nilai ujian
        rata_rata = sum(nilai_ujian) / len(nilai_ujian)
        print(f"Rata-rata nilai ujian: {rata_rata:.2f}")
        # Menampilkan pesan berdasarkan rata-rata nilai ujian
        # Jika rata-rata lebih dari 80, tampilkan pesan "Selamat, Anda lulus!"
        # Jika rata-rata kurang dari atau sama dengan 80, tampilkan pesan "Maaf, Anda tidak lulus."
        if rata_rata > 80:
            print("Selamat, Anda lulus!")
        else:
            print("Maaf, Anda tidak lulus.")