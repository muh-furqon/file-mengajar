# Salah satu jenis perulangan selain while adalah for loop
# For loop digunakan untuk mengulangi blok kode dengan jumlah iterasi yang sudah ditentukan
# Dibandingkan while loop yang terus berjalan sampai kondisi salah (False), for loop lebih terstruktur
# terkontrol, dan lebih mudah dibaca
# Contoh kita ingin mencetak angka dari 1 hingga 10
print("PERNYATAAN FOR")
# Kita bisa menggunakan fungsi range() untuk menghasilkan urutan angka
for i in range(1, 11):
    print(i)

# Contoh kita ingin mencetak angka dari 1 hingga angka yang dimasukkan oleh pengguna
angka = int(input("Masukkan angka: "))
print(f"Angka dari 1 hingga {angka}:")
for i in range(1, angka + 1):
    print(i)

# Kita bisa menggunakan pernyataan break untuk menghentikan perulangan
print("Pernyataan break")
for i in range(1, 11):
    if i == 5:
        break
    print(i)