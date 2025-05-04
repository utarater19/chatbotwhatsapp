# Import Library
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# # Buat data dummy
# data, labels = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# # Visualisasi data awal
# plt.scatter(data[:, 0], data[:, 1], s=50)
# plt.title("Data Sebelum Clustering")
# plt.show()

# # Terapkan algoritma K-Means
# kmeans = KMeans(n_clusters=4, random_state=0)
# kmeans.fit(data)

# # Ambil hasil cluster
# predicted_labels = kmeans.labels_
# centers = kmeans.cluster_centers_

# # Visualisasi hasil clustering
# plt.scatter(data[:, 0], data[:, 1], c=predicted_labels, s=50, cmap='viridis')
# plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X')
# plt.title("Hasil Clustering dengan K-Means")
# plt.show()

import pandas as pd

# Load the CSV file to examine its content
file_path = 'Fintech_user.csv'
data = pd.read_csv (file_path)

# Display the first few rows of the dataframe to understand its structure
print (data)

import matplotlib.pyplot as plt

# Plotting the age distribution
plt.figure(figsize=(10, 6))
plt.hist(data['age'].dropna(), bins=20, edgecolor='k', alpha=0.7)
plt.title('Age Distribution of Users')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(data['credit_score'].dropna(), bins=20, edgecolor='k', alpha=0.7)
plt.title('Credit Score Distribution of Users')
plt.xlabel('Credit Score')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Plotting the relationship between deposits and withdrawals
plt.figure(figsize=(10, 6))
plt.scatter(data['deposits'], data['withdrawal'], alpha=0.6, edgecolor='k')
plt.title('Relationship Between Deposits and Withdrawals')
plt.xlabel('Deposits')
plt.ylabel('Withdrawals')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

#grouping the data by age and calculating the churn rate
churn_rate_by_age = data.groupby('age') ['churn']. mean(). reset_index()

plt.figure(figsize=(10,6))
plt.plot(churn_rate_by_age['age'], churn_rate_by_age['churn'], marker='o')
plt.title(churn_rate_by_age)
plt.xlabel('age')
plt.ylabel('churn rate')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()


import seaborn as sns

# Tampilkan tipe data setiap kolom
print(data.dtypes)

# Pilih hanya kolom numerik untuk correlation matrix
numeric_columns = data.select_dtypes(include=['int64', 'float64']).columns
correlation_matrix = data[numeric_columns].corr()

# Plot correlation matrix
plt.figure(figsize=(15,10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix of Numeric Features')
plt.show()