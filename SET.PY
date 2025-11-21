# 1. MEMBUAT SET
print("1. MEMBUAT SET")
data_kosong = set()        # set kosong harus pakai set(), bukan {}
angka = {1, 2, 3, 4}
campuran = {1, "halo", True, 3.14}
print(data_kosong, angka, campuran)
print("------------------------\n")


# 2. MENAMBAHKAN ITEM
print("2. MENAMBAHKAN ITEM")
angka.add(5)        # tambah 1 item
angka.update([6, 7, 8])   # tambah banyak item
print(angka)
print("------------------------\n")


# 3. MENGHAPUS ITEM
print("3. MENGHAPUS ITEM")
angka.remove(6)     # hapus item tertentu (error jika tidak ada)
angka.discard(10)   # tidak error jika item tidak ada
angka.pop()         # hapus item random
print(angka)

angka.clear()       # hapus semua
print("setelah clear:", angka)
print("------------------------\n")


# 4. LOOPING DALAM SET
print("4. LOOPING DALAM SET")
contoh = {10, 20, 30, 40}
for x in contoh:
    print(x)
print("------------------------\n")


# 5. CEK ITEM DALAM SET
print("5. CEK ITEM")
print(20 in contoh)   # True
print(100 in contoh)  # False
print("------------------------\n")


# 6. UNION (GABUNG SET)
print("6. UNION")
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))     # {1,2,3,4,5}
print("------------------------\n")


# 7. INTERSECTION (IRISAN)
print("7. INTERSECTION")
print(a.intersection(b))   # {3}
print("------------------------\n")


# 8. DIFFERENCE (SELISIH)
print("8. DIFFERENCE")
print(a.difference(b))     # {1,2}
print("------------------------\n")


# 9. SYMMETRIC DIFFERENCE
print("9. SYMMETRIC DIFFERENCE")
print(a.symmetric_difference(b))  # {1,2,4,5}
print("------------------------\n")


# 10. FROZENSET (SET YANG TIDAK BISA DIUBAH)
print("10. FROZENSET")
fs = frozenset([1, 2, 3])
print(fs)
print("------------------------")
