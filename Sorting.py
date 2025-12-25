import time

# ======================================================
# DATA 
# ======================================================
data = [
    72, 15, 93, 44, 55, 18, 67, 12, 88, 39,
    21, 90, 14, 27, 33, 50, 99, 3, 60, 42,
    87, 24, 75, 8, 100, 54, 11, 76, 49, 32,
    95, 23, 7, 65, 58, 17, 82, 34, 29, 40,
    6, 63, 19, 97, 45, 10, 73, 56, 26, 22,
    84, 16, 28, 31, 2, 80, 69, 96, 48, 57,
    9, 25, 98, 59, 43, 5, 13, 20, 153, 61,
    85, 30, 4, 92, 70, 51, 1, 71, 41, 36,
    35, 94, 47, 38, 83, 66, 89, 62, 46, 79,
    78, 52, 91, 86, 68, 77, 74, 64, 81, 37,
    108, 150, 122, 135, 147, 111, 129, 140, 101, 112,
    117, 148, 121, 131, 105, 144, 109, 126, 133, 119
]

# ======================================================
# SORTING ALGORITHMS
# ======================================================

def bubble_sort(arr):
    data = arr.copy()
    for i in range(len(data)):
        for j in range(0, len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def insertion_sort(arr):
    data = arr.copy()
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key
    return data

def selection_sort(arr):
    data = arr.copy()
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)
    return arr

# ======================================================
# SEARCHING ALGORITHMS
# ======================================================

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def binary_search(arr, key):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def hashing_search(arr, key):
    hash_table = {value: i for i, value in enumerate(arr)}
    return hash_table.get(key, -1)

# ======================================================
# TIME CALCULATOR
# ======================================================

def calc_time(func, arr, key=None):
    start = time.time()
    if key is None:
        result = func(arr.copy())
    else:
        result = func(arr.copy(), key) if func == hashing_search else func(arr.copy(), key)
    end = time.time()
    return result, end - start


# ======================================================
# MENU PROGRAM
# ======================================================

while True:
    print("\n===== MENU =====")
    print("1. Sorting")
    print("2. Searching")
    print("3. Keluar")

    menu = input("Pilih menu: ")

    if menu == "1":
        print("\n--- PILIH ALGORITMA SORTING ---")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("3. Selection Sort")
        print("4. Merge Sort")
        print("5. Quick Sort")

        pilih = input("Pilihan algoritma: ")

        algos = {
            "1": bubble_sort,
            "2": insertion_sort,
            "3": selection_sort,
            "4": merge_sort,
            "5": lambda x: quick_sort(x.copy(), 0, len(x)-1)
        }

        algo = algos.get(pilih)

        if algo:
            hasil, waktu = calc_time(algo, data)
            print("\nData sebelum diurutkan:\n", data)
            print("\nHasil sorting:\n", hasil)
            print("\nWaktu eksekusi:", waktu, "detik")
        else:
            print("Pilihan tidak valid.")

    elif menu == "2":
        print("\n--- PILIH ALGORITMA SEARCHING ---")
        print("1. Linear Search")
        print("2. Binary Search")
        print("3. Hashing Search")

        pilih = input("Pilihan algoritma: ")

        key = int(input("Masukkan angka yang dicari: "))

        if pilih == "1":
            pos = linear_search(data, key)
            print("Data:", data)
            print("Hasil:", ("Ditemukan di index " + str(pos)) if pos != -1 else "Tidak ditemukan")

        elif pilih == "2":
            print("\nBinary Search membutuhkan data terurut!")
            sorted_data = merge_sort(data.copy())
            print("Data terurut:", sorted_data)

            pos = binary_search(sorted_data, key)
            print("Hasil:", ("Ditemukan di index " + str(pos)) if pos != -1 else "Tidak ditemukan")

        elif pilih == "3":
            pos = hashing_search(data, key)
            print("Data:", data)
            print("Hasil:", ("Ditemukan di index " + str(pos)) if pos != -1 else "Tidak ditemukan")

        else:
            print("Pilihan tidak valid.")

    elif menu == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")
