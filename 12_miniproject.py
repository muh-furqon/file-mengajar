# Latihan function
# Coba buat aplikasi kalkulator sederhana menggunakan function
# Aplikasi kalkulator sederhana

def tambah(a, b):
    return a + b
def kurang(a, b):
    return a - b
def kali(a, b):
    return a * b
def bagi(a, b):
    if b == 0:
        return "Tidak bisa dibagi dengan nol"
    else:
        return a / b

pilihan_operasi = input("Pilih operasi (+, -, *, /): ")
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
if pilihan_operasi == "+":
    hasil = tambah(angka1, angka2)
elif pilihan_operasi == "-":
    hasil = kurang(angka1, angka2)
elif pilihan_operasi == "*":
    hasil = kali(angka1, angka2)
elif pilihan_operasi == "/":
    hasil = bagi(angka1, angka2)
else:
    hasil = "Operasi tidak valid"
print(f"Hasil: {hasil}")

