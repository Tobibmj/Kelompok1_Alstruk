# 1. MEMBUAT TUPLE
print("1. MEMBUAT TUPLE")
data_kosong = ()
angka = (1, 2, 3, 4)
campuran = (1, "halo", True, 3.14)
satu_item = (5,)   # tuple 1 item harus pakai koma
print(data_kosong, angka, campuran, satu_item)
print("------------------------\n")


# 2. MENGAKSES DATA TUPLE
print("2. MENGAKSES TUPLE")
print(angka[0])     # index 0
print(angka[2])     # index 2
print(angka[-1])    # akses dari belakang
print("------------------------\n")


# 3. SLICING PADA TUPLE
print("3. SLICING TUPLE")
contoh = (10, 20, 30, 40, 50)
print(contoh[1:4])   # 20, 30, 40
print(contoh[:3])    # 10, 20, 30
print(contoh[2:])    # 30, 40, 50
print("------------------------\n")


# 4. LOOPING TUPLE
print("4. LOOPING TUPLE")
for x in contoh:
    print(x)
print("------------------------\n")


# 5. CEK ITEM DALAM TUPLE
print("5. CEK ITEM DALAM TUPLE")
print(20 in contoh)   # True
print(100 in contoh)  # False
print("------------------------\n")


# 6. MENGGABUNGKAN TUPLE
print("6. GABUNGKAN TUPLE")
a = (1, 2, 3)
b = (4, 5)
gabung = a + b
print(gabung)
print("------------------------\n")


# 7. PENGULANGAN TUPLE
print("7. PENGULANGAN TUPLE")
print(a * 3)   # (1,2,3,1,2,3,1,2,3)
print("------------------------\n")


# 8. MENDAPATKAN PANJANG TUPLE
print("8. PANJANG TUPLE")
print(len(contoh))
print("------------------------\n")


# 9. MENGUBAH TUPLE (HARUS DIKONVERSI KE LIST)
print("9. MENGUBAH TUPLE")
x = (1, 2, 3)
y = list(x)        # ubah ke list
y.append(4)        # edit list
x = tuple(y)       # ubah kembali ke tuple
print(x)
print("------------------------\n")


# 10. NESTED TUPLE
print("10. NESTED TUPLE")
nested = (1, (10, 20), 3)
print(nested)
print(nested[1][0])   # akses tuple di dalam tuple
print("------------------------")
