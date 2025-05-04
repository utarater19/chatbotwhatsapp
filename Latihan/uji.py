import matplotlib.pyplot as plt

#Contoh data kependudukan (negara, jumlah penduduk) 
data_kependudukan = [('China', 1439323776), ('India', 1380004385), ('Brazil', 331002651), ('Malysia', 273523615), ('Pakistan', 220892340)]

#Mengurutkan data berdasarkan jumlah penduduk (dari besar ke kecil) 
data_kependudukan.sort(key=lambda x: x[1], reverse=True)

#Mengambil nama negara dan jumlah penduduk untuk menampilkan pada grafik 
negara=[item[0] for item in data_kependudukan] 
jumlah_penduduk=[item[1] for item in data_kependudukan]

#Membuat grafik batang horizontal 
plt.barh(negara, jumlah_penduduk, color='skyblue')

#Mengatur Label sumbu dan judul grafik 
plt.xlabel('Jumlah Penduduk (Milion') 
plt.ylabel('Negara') 
plt.title('Kependudukan di Beberapa Negara')

#Menampilkan grafik 
plt.show()