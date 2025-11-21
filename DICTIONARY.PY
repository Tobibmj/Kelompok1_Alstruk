# 1. MEMBUAT DICTIONARY
print("1. MEMBUAT DICTIONARY")
data = {}
mahasiswa = {
    "nama": "Tobib",
    "umur": 20,
    "prodi": "Informatika"
}
print(data, mahasiswa)
print("------------------------\n")


# 2. MENGAKSES NILAI DALAM DICTIONARY
print("2. MENGAKSES NILAI")
print(mahasiswa["nama"])       # akses langsung
print(mahasiswa.get("prodi"))  # akses 
print("------------------------\n")


# 3. MENAMBAHKAN DATA
print("3. MENAMBAHKAN DATA")
mahasiswa["alamat"] = "Tasikmalaya"
print(mahasiswa)
print("------------------------\n")


# 4. MENGUBAH DATA
print("4. MENGUBAH DATA")
mahasiswa["umur"] = 21
print(mahasiswa)
print("------------------------\n")


# 5. MENGHAPUS DATA
print("5. MENGHAPUS DATA")
mahasiswa.pop("prodi")       # hapus key tertentu
print(mahasiswa)

mahasiswa.popitem()          # hapus item terakhir
print(mahasiswa)

mahasiswa.clear()            # hapus semua data
print("setelah clear:", mahasiswa)
print("------------------------\n")


# 6. MENGECEK KEY DALAM DICTIONARY
print("6. CEK KEY DALAM DICT")
test = {"a": 1, "b": 2}
print("a" in test)     # True
print("z" in test)     # False
print("------------------------\n")


# 7. MENDAPATKAN DAFTAR KEY, VALUE, ITEMS
print("7. KEY, VALUE, ITEMS")
example = {"nama": "Tobib", "job": "Data Analyst"}

print(example.keys())     # semua key
print(example.values())   # semua value
print(example.items())    # pasangan key-value
print("------------------------\n")


# 8. LOOPING DICTIONARY
print("8. LOOPING DICTIONARY")
for key in example:
    print(key, "=", example[key])

for k, v in example.items():
    print(k, "->", v)
print("------------------------\n")


# 9. MENGGABUNGKAN DICTIONARY
print("9. MENGGABUNGKAN DICTIONARY")
a = {"x": 1, "y": 2}
b = {"z": 3}

a.update(b)     # gabung dict b ke a
print(a)
print("------------------------\n")


# 10. NESTED DICTIONARY
print("10. NESTED DICTIONARY")
data_orang = {
    "orang1": {"nama": "Tobib", "umur": 21},
    "orang2": {"nama": "Budi", "umur": 22}
}
print(data_orang)
print(data_orang["orang1"]["nama"])  # akses nested
print("------------------------")
