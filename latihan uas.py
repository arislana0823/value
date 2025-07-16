import time

# Start waktu eksekusi
start_time = time.time()

# ===== Sequence: Input Data Pasien =====
data_pasien = [
    {"nama": "Andi", "penyakit": "Demam", "usia": 25},
    {"nama": "Budi", "penyakit": "Flu", "usia": 32},
    {"nama": "Citra", "penyakit": "Demam", "usia": 18},
    {"nama": "Dina", "penyakit": "Asma", "usia": 45},
    {"nama": "Eko", "penyakit": "Flu", "usia": 28}
]

# ===== Fungsi: Bubble Sort berdasarkan usia =====
def bubble_sort(pasien_list):
    n = len(pasien_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if pasien_list[j]["usia"] > pasien_list[j+1]["usia"]:
                pasien_list[j], pasien_list[j+1] = pasien_list[j+1], pasien_list[j]
    return pasien_list

# ===== Fungsi Rekursif: Hitung jumlah pasien dengan penyakit tertentu =====
def hitung_penyakit(pasien_list, penyakit_dicari, index=0):
    if index == len(pasien_list):
        return 0
    count = 1 if pasien_list[index]["penyakit"] == penyakit_dicari else 0
    return count + hitung_penyakit(pasien_list, penyakit_dicari, index + 1)

# ===== Proses: Urutkan dan hitung penyakit =====
data_terurut = bubble_sort(data_pasien)
jumlah_flu = hitung_penyakit(data_terurut, "Flu")

# ===== Output: Tampilkan data =====
print("Data Pasien Setelah Diurutkan Berdasarkan Usia:")
for pasien in data_terurut:
    print(f"- {pasien['nama']}, Usia: {pasien['usia']}, Penyakit: {pasien['penyakit']}")

print(f"\nJumlah pasien dengan penyakit 'Flu': {jumlah_flu}")

# ===== Hitung dan tampilkan waktu eksekusi =====
end_time = time.time()
print(f"\nWaktu eksekusi program: {end_time - start_time:.6f} detik")
