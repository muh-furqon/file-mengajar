# Dalam pemrograman, kita bisa menggunakan input dan output untuk berinteraksi dengan pengguna.
# Input adalah cara untuk mendapatkan data dari pengguna
# Output adalah cara untuk menampilkan data ke pengguna
# Pada Python, kita bisa menggunakan fungsi input() untuk mendapatkan input dari pengguna

# Fungsi input() akan menampilkan pesan ke layar dan menunggu pengguna untuk memasukkan data
# Fungsi input() akan mengembalikan data yang dimasukkan oleh pengguna dalam bentuk string
# Kita bisa menggunakan fungsi print() untuk menampilkan data ke layar

namaku = input("Masukkan nama kamu: ")
print("Halo " + namaku)

# Fungsi input() juga bisa digunakan untuk mendapatkan input dari pengguna dalam bentuk angka
# Namun, kita perlu mengkonversi data yang dimasukkan oleh pengguna ke dalam tipe data yang sesuai
# Kita bisa menggunakan fungsi int() untuk mengkonversi string ke integer
angka1 = input("Masukkan angka pertama: ")
angka1 = int(angka1)
angka2 = input("Masukkan angka kedua: ")
angka2 = int(angka2)
jumlah = angka1 + angka2
print("Jumlah dari " + str(angka1) + " dan " + str(angka2) + " adalah " + str(jumlah))
# Kita bisa menggunakan fungsi str() untuk mengkonversi angka ke string
huruf = str(jumlah)
tipe = type(huruf)
print("Ini tipe data jumlah kalau kita masukkan ke str() " + str(tipe))
# Kita bisa menggunakan fungsi float() untuk mengkonversi string ke float
angka3 = input("Masukkan angka ketiga: ")
print(type(angka3))
angka3 = float(angka3)
print("Ini tipe data angka3 kalau kita masukkan ke float() " + str(type(angka3)))