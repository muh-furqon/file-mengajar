# Latihan function
# Buat function untuk menghitung penjumlahan dua angka
def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

pilihan = input("Pilih operasi (1: Penjumlahan, 2: Pengurangan, 0: Keluar): ")
while pilihan != '0':
    if pilihan not in ['1', '2']:
        print("Pilihan tidak valid. Silakan coba lagi.")
    else:
        if pilihan == '1':
            a = int(input("Masukkan angka pertama: "))
            b = int(input("Masukkan angka kedua: "))
            print("Hasil penjumlahan:", penjumlahan(a, b))
        elif pilihan == '2':
            a = int(input("Masukkan angka pertama: "))
            b = int(input("Masukkan angka kedua: "))
            print("Hasil pengurangan:", pengurangan(a, b))
    
    pilihan = input("Pilih operasi (1: Penjumlahan, 2: Pengurangan, 0: Keluar): ")