# Dalam pemrograman, kita sering kali perlu melakukan perulangan untuk mengulangi suatu blok kode
# Umumnya, orang orang akan mengetik ulang kode yang sama berulang kali
# Namun, ini bukanlah cara yang efisien
# Kita bisa menggunakan pernyataan while untuk melakukan perulangan
# Pernyataan while akan terus mengeksekusi blok kode selama kondisi yang diberikan benar (True)
# Jika kondisi tersebut salah (False), maka perulangan akan berhenti
# Kita bisa menggunakan pernyataan break untuk menghentikan perulangan
# Kita juga bisa menggunakan pernyataan continue untuk melanjutkan ke iterasi berikutnya

print("PERNYATAAN WHILE")
angka = int(input("Masukkan angka (0 untuh berhenti): "))

while angka != 0:
    if angka % 2 == 0:
        print(f"{angka} adalah angka genap")
    else:
        print(f"{angka} adalah angka ganjil")
    angka = int(input("Masukkan angka (0 untuh berhenti): "))