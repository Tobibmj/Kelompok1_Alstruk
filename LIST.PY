# 1. MEMBUAT LIST
print("1. MEMBUAT LIST")
data_kosong = []
angka = [1, 2, 3, 4]
campuran = [1, "halo", True, 3.14]
print(data_kosong, angka, campuran)
print("------------------------\n")


# 2. MENGAKSES ITEM LIST
print("2. MENGAKSES ITEM LIST")
print(angka[0])     # index 0
print(angka[2])     # index 2
print(angka[-1])    # item terakhir
print("------------------------\n")


# 3. MENGUBAH NILAI
print("3. MENGUBAH NILAI")
angka[1] = 200
print(angka)
print("------------------------\n")


# 4. MENAMBAHKAN ITEM
print("4. MENAMBAHKAN ITEM")
angka.append(5)
angka.insert(1, 100)
angka.extend([6, 7, 8])
print(angka)
print("------------------------\n")


# 5. MENGHAPUS ITEM
print("5. MENGHAPUS ITEM")
angka.remove(100)
angka.pop(0)
angka.pop()
print(angka)
angka.clear()
print("setelah clear:", angka)
print("------------------------\n")


# 6. PANJANG LIST
print("6. PANJANG LIST")
contoh = [10, 20, 30, 40, 50]
print("len:", len(contoh))
print("------------------------\n")


# 7. SLICING LIST
print("7. SLICING LIST")
print(contoh[1:4])   # 20, 30, 40
print(contoh[:3])    # 10, 20, 30
print(contoh[2:])    # 30, 40, 50
print("------------------------\n")


# 8. LOOPING LIST
print("8. LOOPING LIST")
for x in contoh:
    print(x)
print("------------------------\n")


# 9. CEK ITEM DALAM LIST
print("9. CEK ITEM DALAM LIST")
print(20 in contoh)
print(100 in contoh)
print("------------------------\n")


# 10. SORT & REVERSE
print("10. SORT & REVERSE")
nilai = [5, 3, 8, 1]
nilai.sort()
print("sorted:", nilai)
nilai.reverse()
print("reversed:", nilai)
print("------------------------")
