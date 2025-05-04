# Import Library
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Buat data dummy
data, labels = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Visualisasi data awal
plt.scatter(data[:, 0], data[:, 1], s=50)
plt.title("Data Sebelum Clustering")
plt.show()

# Terapkan algoritma K-Means
kmeans = KMeans(n_clusters=4, random_state=0)
kmeans.fit(data)

# Ambil hasil cluster
predicted_labels = kmeans.labels_
centers = kmeans.cluster_centers_

# Visualisasi hasil clustering
plt.scatter(data[:, 0], data[:, 1], c=predicted_labels, s=50, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X')
plt.title("Hasil Clustering dengan K-Means")
plt.show()