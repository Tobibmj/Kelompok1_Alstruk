# Tugas Algoritma dan struktur data
MENU_HARGA = {
    # Makanan (Sudah termasuk free es teh manis)
    "ayam goreng": 15000,
    "ayam bakar": 15000,
    "ayam ungkep": 15000,
    "pepes ayam": 15000,
    
    # Sambel
    "sambel matah": 5000,
    "sambel ijo": 5000,
    "sambel terasi": 5000,
    "sambel teri": 5000,
    "sambal bakar": 5000, 
    "sambel bakar": 5000,
    "sambel cumi": 5000,
    
    # Nasi
    "nasi putih": 6000,
    "nasi liwet": 6000,
    "nasi to": 6000,
    "nasi kuning": 6000,
    "nasi merah": 8000,
    
    # Minuman (Es teh manis gratis jika pesan ayam)
    "es campur": 5000,
    "es buah": 10000,
    "sop durian": 25000,
    "es tebu": 7000,
    "es teler": 10000,
    "es dawet": 5000,
    
    # Camilan
    "citul": 5000,
    "puding": 5000,
    "ice cream": 5000,
}

# --- FUNGSI UNTUK MENAMPILKAN MENU  ---
# def tampilkan_menu adalah blok kode yang berisi semua perintah print untuk menampilkan daftar menu. 
# blok ini diberi nama tampilkan_menu, blok ini tidak akan berjalan sampai ada yang memanggil namanya.
def tampilkan_menu():
    """Mencetak daftar menu agar mudah dibaca oleh kasir."""
    print("=" * 40)
    print("      MENU RUMAH MAKAN NGODING SEUBEUH")
    print("=" * 40)
    
    print("\n--- Makanan (All Variant Rp 15.000) ---")
    print("   (Free Es Teh Manis)")
    print("1. Ayam Goreng")
    print("2. Ayam Bakar")
    print("3. Ayam Ungkep")
    print("4. Pepes Ayam")
    
    print("\n--- Sambel (All Variant Rp 5.000) ---")
    print("1. Sambel Matah")
    print("2. Sambel Ijo")
    print("3. Sambel Terasi")
    print("4. Sambel Teri")
    print("5. Sambel Bakar")
    print("6. Sambel Cumi")
    
    print("\n--- Nasi ---")
    print("1. Nasi Putih   (Rp 6.000)")
    print("2. Nasi Liwet   (Rp 6.000)")
    print("3. Nasi TO      (Rp 6.000)")
    print("4. Nasi Kuning  (Rp 6.000)")
    print("5. Nasi Merah   (Rp 8.000)")
    
    print("\n--- Minuman ---")
    print("1. Es Campur    (Rp 5.000)")
    print("2. Es Buah      (Rp 10.000)")
    print("3. Sop Durian   (Rp 25.000)")
    print("4. Es Tebu      (Rp 7.000)")
    print("5. Es Teler     (Rp 10.000)")
    print("6. Es Dawet     (Rp 5.000)")
    
    print("\n--- Camilan (All Variant Rp 5.000) ---")
    print("1. Citul")
    print("2. Puding")
    print("3. Ice Cream")
    print("=" * 40)

# --- FUNGSI UTAMA KALKULATOR ---
# def jalankan_kasir() adalah blok kode utama yang berisi semua logika kasir (menghitung total, meminta input, dsb.)
# di dalam def jalankan_kasir(), ada satu baris kode yang tertulis: tampilkan_menu(), Baris yang memanggil blok def tampilkan_menu().
# Jadi urutannya:
# 1.Program utama memanggil jalankan_kasir().
# 2.Kode jalankan_kasir() mulai berjalan.
# 3.Saat sampai di baris tampilkan_menu(), program "melompat" dan menjalankan semua perintah print di dalam def tampilkan_menu().
# 4.Setelah selesai, program "kembali" ke jalankan_kasir() dan melanjutkan sisa perintahnya (meminta input, dsb.).
def jalankan_kasir():
    """Fungsi utama untuk menjalankan aplikasi kasir."""
    
    # List untuk menyimpan semua pesanan. 
    # di simpan sebagai dictionary per pesanan.
    pesanan = [] 
    total_harga = 0
    ada_pesanan_ayam = False # Penanda untuk free es teh

    tampilkan_menu()
    print("\nSilakan masukkan pesanan satu per satu.")
    print("Ketik 'selesai' pada nama menu jika sudah selesai.")
    print("-" * 40)

    while True:
        # 1. Minta input nama menu
        # .lower() digunakan agar input "Ayam Goreng" atau "ayam goreng" sama saja
        nama_menu = input("Nama Menu: ").lower()

        if nama_menu == 'selesai':
            break # Keluar dari loop jika input adalah 'selesai'

        # 2. Cek apakah menu ada di dictionary
        if nama_menu in MENU_HARGA:
            # 3. Minta input jumlah
            try:
                jumlah = int(input(f"Jumlah {nama_menu}: "))
                if jumlah <= 0:
                    print("Jumlah harus lebih dari 0. Silakan ulangi menu.")
                    continue # Kembali ke awal loop
                    
            except ValueError:
                print("Input jumlah tidak valid. Silakan ulangi menu.")
                continue # Kembali ke awal loop

            # 4. Hitung subtotal dan tambahkan ke total
            harga_satuan = MENU_HARGA[nama_menu]
            subtotal = harga_satuan * jumlah
            total_harga += subtotal

            # 5. Simpan pesanan untuk struk
            pesanan.append({
                "nama": nama_menu.title(), # .title() untuk cetak (e.g., "Ayam Goreng")
                "jumlah": jumlah,
                "subtotal": subtotal
            })
            
            # 6. Cek apakah ada pesanan ayam untuk free es teh
            if "ayam" in nama_menu or "pepes" in nama_menu:
                ada_pesanan_ayam = True

            print(f"-> {jumlah} {nama_menu.title()} ditambahkan. Total sementara: Rp {total_harga:,.0f}\n")
            # Huruf f di depan tanda kutip mengubah string biasa menjadi "f-string". Ini mengizinkan kita memasukkan variabel langsung ke dalam teks menggunakan kurung kurawal { }.
            # .title = Ini adalah method (fungsi bawaan) untuk string yang mengubah teks menjadi "Title Case" (huruf pertama setiap kata jadi kapital)
            # total_harga:,.0f = Ini adalah bagian yang paling canggih. Ini mengambil nilai dari variabel total_harga (misalnya, 30000) dan memformatnya:

        else:
            print(f"** Maaf, menu '{nama_menu}' tidak ditemukan. Silakan coba lagi. **\n")

    # --- CETAK STRUK ---
    if not pesanan:
        print("\nBelum ada pesanan yang dimasukkan.")
        return
    # return Itu hanya akan berfungsi jika kasir langsung mengetik "selesai" sebelum memasukkan satu menu pun.
    #Tujuannya adalah agar program tidak melanjutkan ke kode-kode di bawahnya (yaitu kode print("STRUK PEMBAYARAN"), for item in pesanan:, print("TOTAL HARGA"),dll

    print("\n" + "=" * 40)
    print("     STRUK PEMBAYARAN - NGODING SEUBEUH")
    print("=" * 40)
    print(f"{'Menu':<20} {'Jml':<4} {'Subtotal':>13}")
    print("-" * 40)

    for item in pesanan:
        # f-string formatting:
        # <20 = Rata kiri selebar 20 karakter
        # <4  = Rata kiri selebar 4 karakter
        # >13 = Rata kanan selebar 13 karakter, format ribuan (,)
        print(f"{item['nama']:<20} {item['jumlah']:<4} Rp{item['subtotal']:>10,.0f}")

    if ada_pesanan_ayam:
        print("-" * 40)
        print(f"* Free Es Teh Manis (Bonus Pesanan Ayam)")
    
    print("=" * 40)
    # Cetak total akhir
    '''Tanda , (koma) dipakai sebagai pemisah ribuan (misalnya, 75000 jadi 75,000), 
    dan .0f memastikan angka itu dicetak sebagai bilangan bulat tanpa ada angka desimal di belakang koma.'''
    print(f"{'TOTAL HARGA':<24} Rp{total_harga:>13,.0f}") 
    print("=" * 40)
    print("       Terima kasih atas kunjungan Anda!")
    print("=" * 40)


# --- Mulai program ---
'''Baris kode itu adalah cara standar di Python untuk bilang:
"Jika file ini adalah program utama yang sedang dijalankan, maka mulailah dengan memanggil fungsi jalankan_kasir()."
Tanpa jalankan_kasir() di dalam if itu, programmu hanya akan membaca semua resep (def) dan menyimpannya di memori, tapi tidak pernah memulai "resep utama" kasirnya.'''
if __name__ == "__main__":
    jalankan_kasir()