# Dalam pemrograman, kita bisa menggunakan percabangan untuk mengambil keputusan berdasarkan kondisi tertentu.
# Percabangan adalah cara untuk menentukan jalur eksekusi program berdasarkan kondisi yang diberikan
# Dalam Python, kita bisa menggunakan pernyataan if untuk membuat percabangan
# Pernyataan if akan mengevaluasi kondisi yang diberikan
# Jika kondisi tersebut benar (True), maka blok kode di dalam pernyataan if akan dieksekusi
# Jika kondisi tersebut salah (False), maka blok kode di dalam pernyataan else akan dieksekusi
print("PERNYATAAN IF")
if 5 > 3:
    print("Lima lebih besar dari tiga")
    print("Kode if ini akan dieksekusi")
else:
    print("Lima tidak lebih besar dari tiga")

# Kita bisa menggunakan pernyataan else untuk menangani kondisi yang tidak terpenuhi
# Pernyataan else akan dieksekusi jika semua kondisi sebelumnya salah (False)

print()
print("PERNYATAAN ELSE")
if 5 < 3:
    print("Lima lebih kecil dari tiga") 
else:
    print("Lima tidak lebih kecil dari tiga")
    print("Kode else ini akan dieksekusi")

# Kita bisa menggunakan pernyataan elif untuk mengevaluasi beberapa kondisi
# Pernyataan elif akan dieksekusi jika kondisi sebelumnya salah (False) dan kondisi elif benar (True)
print()
print("PERNYATAAN ELIF")
if 5 < 3:
    print("Lima lebih kecil dari tiga")
    print("Kode if ini tidak akan dieksekusi")
elif 5 > 3:
    print("Lima lebih besar dari tiga")
    print("Kode elif ini akan dieksekusi")
else:
    print("Lima sama dengan tiga")
    print("Kode else ini tidak akan dieksekusi")

# Kita bisa menggunakan operator logika untuk menggabungkan beberapa kondisi
# Operator logika terdiri dari AND, OR, dan NOT
# Operator AND akan mengembalikan True jika kedua kondisi benar (True)
print()
print("OPERATOR LOGIKA")
print()
print("Operator AND")
if 5 > 3 and 3 < 5:
    print("Lima lebih besar dari tiga dan tiga lebih kecil dari lima")
# Operator OR akan mengembalikan True jika salah satu kondisi benar (True)
print("Operator OR")
if 5 > 3 or 3 > 5:
    print("Lima lebih besar dari tiga atau tiga lebih besar dari lima")
# Operator NOT akan mengembalikan True jika kondisi salah (False)
print("Operator NOT")
if not (5 < 3):
    print("Lima tidak lebih kecil dari tiga")

# Kita juga bisa menggunakan pernyataan if dalam satu baris
# Pernyataan if dalam satu baris akan dieksekusi jika kondisi benar (True)
print("Pernyataan if dalam satu baris")
if 5 > 3: print("Lima lebih besar dari tiga")
# Contoh lain
print("Contoh lain")
umur = 17
if umur >= 17:
    print("bisa membuat KTP")
else:
    print("belum bisa membuat KTP")

hujan = True
if hujan:
    print("bawa payung cuy")
else:
    print("tidak usah bawa payung cuy")

ujian = False
if ujian:
    print("selamat ujian")
else:
    print("selamat liburan")