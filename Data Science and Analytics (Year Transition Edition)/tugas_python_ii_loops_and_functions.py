# -*- coding: utf-8 -*-
"""Tugas Python II - Loops and Functions

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11LexoKODi8TEXnHdElSywspUohRREWhA

1. Dari list berikut

  numbers = [4, 5, 10, 20, 40, 60, 80]

  Buat list baru "new_list" yang terdiri dari angka yang lebih besar dari 10
"""

numbers = [4, 5, 10, 20, 40, 60, 80]

new_list = []
for n in numbers:
  if n > 10:
    new_list.append(n)

print(new_list)

"""2. Buatlah sebuah fungsi untuk mencari luas sebuah lingkaran. Gunakan r sebagai input di parameter"""

def circle_area(r):
  pi = 3.14
  area = pi * (r**2)
  return area

print(circle_area(10))
print(circle_area(4))

"""3. Buatlah sebuah fungsi untuk menambahkan dua buah angka (a dan b) dan print:
  - Penjumlahan dari kedua angka
  - Perkalian dari kedua angka
  - Angka tertinggi
"""

def angka(a, b):
  jumlah = a + b
  perkalian = a * b
  tertinggi = max(a, b)

  print(f"{a} + {b} = {jumlah}")
  print(f"{a} * {b} = {perkalian}")
  print(f"Angka tertinggi adalah {tertinggi}")

angka(3, 5)

"""4. Simulasi pesanan kasir"""

menus = [
    {
        "name": "Ayam Goreng",
        "price": 10000
    },
    {
        "name": "Nasi Putih",
        "price": 5000
    },
    {
        "name": "Urap",
        "price": 8000
    },
    {
        "name": "Es Teh",
        "price": 4000
    }
]

nama = input("Nama pelanggan: ")
menu_dipesan = []
menu_dipesan_all = []
total_harga = 0

for menu in menus:
  menu_dipesan_all.append(menu["name"])

while True:
  pesanan = input("Input pesanan di sini: ")
  if pesanan in menu_dipesan_all:
    menu_dipesan.append(pesanan)
    for menu in menus:
      if menu["name"] == pesanan:
        total_harga += menu["price"]
  else:
    print("Maaf menu tidak tersedia")

  print("Apakah sudah selesai? 'Ya/Tidak'")
  done = input()

  if done == "Ya":
    break

print("  ")
print(f"Pesanan customer {nama} adalah {', '.join(menu_dipesan)}")
print(f"Jumlah yang harus dibayar untuk {len(menu_dipesan)} buah menu adalah Rp {total_harga}")

