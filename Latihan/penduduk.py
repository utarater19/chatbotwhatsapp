import matplotlib.pyplot as plt

# Contoh data kependudukan (Provinsi, jumlah penduduk) 
data_kependudukan = [
    ('Kota Ternate', 206745),
    ('Kota Kepulauan Tidore', 118247),
    ('Kabupaten Halmahera Barat', 137541),
    ('Kabupaten Halmahera Selatan', 255795),
    ('Kabupaten Halmahera Tengah', 59096),
    ('Kabupaten Halmahera Utara', 202755),
    ('Kabupaten Halmahera Timur', 94510),
    ('Kabupaten Kepulauan Sula', 106778),
    ('Kabupaten Pulau Taliabu', 59601),
    ('Kabupaten Pulau Morotai', 78270)
]

# Mengurutkan data berdasarkan jumlah penduduk (dari besar ke kecil) 
data_kependudukan.sort(key=lambda x: x[1], reverse=True)

# Mengambil nama provinsi dan jumlah penduduk untuk menampilkan pada grafik 
provinsi = [item[0] for item in data_kependudukan]
jumlah_penduduk = [item[1] for item in data_kependudukan]

# Konversi nama provinsi ke posisi untuk sumbu y
posisi = range(len(provinsi))

# Membuat scatter plot
plt.scatter(jumlah_penduduk, posisi, color='skyblue', s=400)  # `s` untuk ukuran titik

# Menampilkan label provinsi pada sumbu y
plt.yticks(posisi, provinsi)

# Mengatur label sumbu dan judul grafik
plt.xlabel('Jumlah Penduduk')
plt.ylabel('Provinsi')
plt.title('Kependudukan Kabupaten/Kota di Provinsi Maluku Utara')

# Menampilkan grid untuk sumbu x
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Menampilkan grafik
plt.show()
