# 1. MEMBUAT FUNCTION SEDERHANA
print("1. FUNCTION SEDERHANA")
def halo():
    print("Halo, Tobib!")

halo()
print("------------------------\n")


# 2. FUNCTION DENGAN PARAMETER
print("2. FUNCTION DENGAN PARAMETER")
def sapa(nama):
    print("Halo", nama)

sapa("Tobib")
print("------------------------\n")


# 3. FUNCTION DENGAN RETURN NILAI
print("3. FUNCTION DENGAN RETURN")
def tambah(a, b):
    return a + b

hasil = tambah(5, 3)
print("Hasil:", hasil)
print("------------------------\n")


# 4. PARAMETER DEFAULT
print("4. PARAMETER DEFAULT")
def greet(nama="Tobib"):
    print("Halo", nama)

greet()
greet("Budi")
print("------------------------\n")


# 5. PARAMETER TAK TERBATAS (args)
print("5. ARGS (ARGUMENT TAK TERBATAS)")
def jumlahkan(*angka):
    total = sum(angka)
    print("Total:", total)

jumlahkan(1, 2, 3, 4)
print("------------------------\n")


# 6. PARAMETER KEYWORD TAK TERBATAS (kwargs)
print("6. KWARGS")
def biodata(**data):
    for key, value in data.items():
        print(key, ":", value)

biodata(nama="Tobib", umur=20, prodi="Informatika")
print("------------------------\n")


# 7. RETURN BANYAK NILAI
print("7. RETURN MULTIPLE VALUE")
def operasi(a, b):
    return a + b, a - b, a * b

tambah_, kurang_, kali_ = operasi(10, 5)
print(tambah_, kurang_, kali_)
print("------------------------\n")


# 8. LAMBDA FUNCTION (FUNCTION SINGKAT)
print("8. LAMBDA FUNCTION")
kali = lambda x: x * 2
print(kali(10))
print("------------------------\n")


# 9. FUNCTION DALAM FUNCTION (NESTED)
print("9. NESTED FUNCTION")
def luar():
    print("Ini function luar")

    def dalam():
        print("Ini function dalam")

    dalam()

luar()
print("------------------------\n")


# 10. RECURSION (FUNCTION MEMANGGIL DIRI SENDIRI)
print("10. RECURSION")
def hitung_mundur(n):
    if n == 0:
        print("Selesai!")
    else:
        print(n)
        hitung_mundur(n - 1)

hitung_mundur(5)
print("------------------------")
