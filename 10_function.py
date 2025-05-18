# Tahu kenapa ketika kita ingin mengurutkan nilai dalam list kita harus menggunakan sort()?
# Dan tahu kenapa Python langsung mengurutkan list dari yang terkecil ke yang terbesar?
# Kenapa kita tidak mengetik proses pengurutan secara manual?
# Karena sort() adalah sebuah fungsi
# Fungsi adalah sekumpulan kode yang dapat digunakan kembali untuk melakukan tugas tertentu
# Fungsi memungkinkan kita untuk mengelompokkan kode yang sering digunakan dalam satu tempat
# Fungsi juga memungkinkan kita untuk menghindari penulisan kode yang berulang-ulang
# Fungsi juga memungkinkan kita untuk membuat kode yang lebih terstruktur dan mudah dibaca
# Fungsi juga memungkinkan kita untuk membuat kode yang lebih efisien dan mudah dipelihara
# Fungsi juga memungkinkan kita untuk membuat kode yang lebih modular dan dapat digunakan kembali
# Fungsi juga memungkinkan kita untuk membuat kode yang lebih fleksibel dan dapat disesuaikan
# Fungsi juga memungkinkan kita untuk membuat kode yang lebih mudah dipahami dan di-debug
# Fungsi juga memungkinkan kita untuk membuat kode yang lebih mudah diuji dan dioptimalkan

# Contoh fungsi sederhana
def halo():
    print("Halo, selamat datang di Python!")
    print("Ini adalah fungsi sederhana yang mencetak pesan.")

# Memanggil fungsi halo
halo()

# Membuat fungsi penjumlahan
def penjumlahan(a, b):
    return a + b
# Memanggil fungsi penjumlahan
hasil = penjumlahan(5, 3)
print(f"Hasil penjumlahan 5 dan 3 adalah: {hasil}")

# Membuat fungsi dengan parameter default
def perkalian(a, b):
    return a * b

# Contoh kita memasukkan 2 angka sendiri untuk dijumlahkan

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
# Memanggil fungsi penjumlahan
hasil = penjumlahan(a, b)
print(f"Hasil penjumlahan {a} dan {b} adalah: {hasil}")

# Contoh kita memasukkan 2 angka sendiri untuk dikalikan
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
# Memanggil fungsi perkalian
hasil = perkalian(a, b)
print(f"Hasil perkalian {a} dan {b} adalah: {hasil}")