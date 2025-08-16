# 1. Rancang Logika Dasar
# Sebelum menulis kode, pikirkan alur programnya. Kalkulator kita akan:
# Meminta pengguna memasukkan angka pertama.
# Meminta pengguna memasukkan operator (seperti +, -, *, /).
# Meminta pengguna memasukkan angka kedua.
# Menganalisis operator yang dimasukkan dan melakukan perhitungan yang sesuai.
# Mencetak hasilnya.

angka1 = float(input("Masukkan Angka Pertama: "))
angka2 = float(input("Masukkan Angka Kedua: "))

operator = input("Masukkan Operator Perhitungan (+, -, *, /): ")

def calculate():
    if operator == "+":
        hasil = angka1 + angka2
    elif operator == "-":
        hasil = angka1 - angka2
    elif operator == "*":
        hasil = angka1 * angka2
    elif operator == "/":
        if angka2 == 0:
            print("Error: Tidak bisa membagi dengan nol!")
        else:
            hasil = angka1 / angka2
    else:
        print("Error: Inputan yang masuk tidak sesuai!")
    
    if hasil is not None:
        print(f"Hasil perhitungan: {hasil}")

calculate()