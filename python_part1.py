# -*- coding: utf-8 -*-
"""python_part1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1t-TxBejh4Uq18bo2MhkjtGJ3Sm8ooVl_

cek versi python
"""

!python --version

"""menampilkan teks

"""

print("halooo...")
print("mari menjinakan python")

"""variable dan tipe data

gaya penulisan variable
1. snake case = nama_depan
2. camel case = namaDepan
3. all caps = NAMADEPAN
"""

#membuat variable
nama_mahasiswa = "Muhammad Irfan"
NIM = 240101010025
programStudi = "Sistem Informasi"
ipk = 3.85
statusKelulusan = False

#cek tipe data variable
print(type(nama_mahasiswa))
print(type(NIM))
print(type(programStudi))
print(type(ipk))
print(type(statusKelulusan))

pesan1 = "Selamat Datang"
pesan2 = "Mari Bermain Python"
print(pesan1)
print(pesan2)

#mengubah isi pesan2 menjadi isi pesan1
pesan2 = pesan1
print(pesan2)

"""Input dengan data string"""

print("Selamat Datang Mahasiswa")

#minta input data mahasiswa
nama_mahasiswa = input("Masukkan nama : ")
NIM = input("Masukkan NIM : ")

#output
print()
print("========== Data Mahasiswa ==========")
print("Nama Mahasiswa: ", nama_mahasiswa)
print("NIM : ", NIM)

"""Input dengan data integer"""

#masukkan ukuran persegi panjang
panjang = int(input("Masukkan panjang persegi panjang: "))
lebar = int(input("Masukkan lebar persegi panjang: "))

#hitung luas persegi panjang
luas  = panjang * lebar
print("Luas Persegi Panjang adalah: ", luas)

"""sub string"""

nama = "Muhammad Irfan Maulana"
print(nama[0])

abjad = "abcdefghijklmnopqrstuvwxyz"
panjangAbjad = len(abjad)
print(panjangAbjad)
print(abjad[:6])
print(abjad[3:])
print(abjad[1:3])

"""new line (\n)"""

teks = "Yth, \nBapak/Ibu HRD \ndi tempat"
print(teks)