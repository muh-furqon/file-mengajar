# Dalam pemrograman, terkadang kita perlu menyimpan beberapa nilai dalam satu variabel
# Python menyediakan beberapa struktur data untuk menyimpan beberapa nilai dalam satu variabel
# Salah satu struktur data yang paling umum digunakan adalah list
# List adalah kumpulan dari beberapa nilai yang disimpan dalam satu variabel
# List dapat menyimpan berbagai jenis data, seperti angka, string, dan objek lainnya
# List juga dapat menyimpan nilai yang berbeda-beda dalam satu list
# List dapat diubah (mutable), artinya kita dapat menambahkan, menghapus, atau mengubah nilai dalam list
# List dapat diakses menggunakan indeks, yang dimulai dari 0
# Kita dapat menggunakan fungsi len() untuk mendapatkan panjang list
list_angka = [1, 2, 3, 4, 5]
print("List angka:", list_angka)
print("Panjang list angka:", len(list_angka))
# Kita dapat menggunakan fungsi append() untuk menambahkan nilai ke dalam list
list_angka.append(6)
print("List angka setelah ditambahkan 6:", list_angka)
# Kita dapat menggunakan fungsi extend() untuk menambahkan beberapa nilai ke dalam list
list_angka.extend([7, 8, 9])
print("List angka setelah ditambahkan 7, 8, 9:", list_angka)
# Kita dapat menggunakan fungsi insert() untuk menyisipkan nilai ke dalam list pada indeks tertentu
list_angka.insert(0, 0)
print("List angka setelah disisipkan 0 di indeks 0:", list_angka)
# Kita dapat menggunakan fungsi remove() untuk menghapus nilai dari list
list_angka.remove(5)
print("List angka setelah dihapus 5:", list_angka)
# Kita dapat menggunakan fungsi pop() untuk menghapus nilai dari list berdasarkan indeks
list_angka.pop(0)
print("List angka setelah dihapus indeks 0:", list_angka)
# Kita dapat menggunakan fungsi index() untuk mendapatkan indeks dari nilai dalam list
indeks_3 = list_angka.index(3)
print("Indeks dari 3 dalam list angka:", indeks_3)
# Kita dapat menggunakan fungsi count() untuk menghitung jumlah kemunculan nilai dalam list
list_angka_baru = [1, 2, 3, 3, 4, 5]
print("List angka baru:", list_angka_baru)
jumlah_3 = list_angka.count(3)
print("Jumlah kemunculan 3 dalam list angka baru:", jumlah_3)
# Kita dapat menggunakan fungsi sort() untuk mengurutkan list
list_angka_acak = [5, 3, 1, 4, 2]
list_angka_baru.sort()
print("List angka acak setelah diurutkan:", list_angka_baru)
# Kita dapat menggunakan fungsi reverse() untuk membalik urutan list
list_angka_baru.reverse()
print("List angka baru setelah dibalik urutannya:", list_angka_baru)
# Kita dapat menggunakan fungsi sum() untuk menjumlahkan semua nilai dalam list
jumlah_list_angka = sum(list_angka_baru)
print("Jumlah semua nilai dalam list angka baru:", jumlah_list_angka)

# Kita bisa menggunakan pernyataan for untuk mengulangi setiap nilai dalam list
print("Mengulangi setiap nilai dalam list angka baru:")
for angka in list_angka_baru:
    print(angka)

# List juga dapat menyimpan nilai yang berbeda-beda dalam satu list
list_kombinasi = [1, "dua", 3.0, True]
print("List kombinasi:", list_kombinasi)
# Kita dapat menggunakan fungsi type() untuk mendapatkan tipe data dari setiap nilai dalam list
for nilai in list_kombinasi:
    print(f"Nilai: {nilai}, Tipe data: {type(nilai)}")

