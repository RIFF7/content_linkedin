# Rancang Logika Dasar
# Sama seperti sebelumnya, kita mulai dengan merancang alur programnya.
# Program akan "memikirkan" sebuah angka rahasia secara acak.
# Pengguna diminta untuk menebak angka tersebut.
# Jika tebakan salah, program akan memberi petunjuk apakah tebakan terlalu tinggi atau terlalu rendah.
# Langkah 2 dan 3 akan diulang sampai tebakan pengguna benar.
# Setelah benar, program akan memberi selamat kepada pengguna dan memberi tahu berapa kali tebakan yang dilakukan.

import random

# 1. Hasilkan angka rahasia
angka_rahasia = random.randint(1, 100)

percobaan = 0
tebakan = 0

print("Selamat datang di Permainan Tebak Angka! 🎮")
print("System telah memilih angka acak dari 1 sampai 100, coba tebak!")

while tebakan != angka_rahasia:
    try:
        # Masukkan tebakan kamu
        tebakan = int(input("Masukkan tebakan angka kamu 🤗: "))
        percobaan += 1
        
        # Berikan petunjuk pada pemain
        if tebakan < angka_rahasia:
            print("Terlalu rendah! 📉 Coba tebak lagi")
        elif tebakan > angka_rahasia:
            print("Kali ini terlalu tinggi! 📈 Coba tebak lagi 😂")
        else:
            print(f"Selamat tebakan kamu BENAR {tebakan} ✨✨🎉 Kamu berhasil pada percobaan ke-{percobaan} 😂")
    except ValueError:
        print("Inputan yang kamu masukkan tidak sesuai, coba kembali ya!")