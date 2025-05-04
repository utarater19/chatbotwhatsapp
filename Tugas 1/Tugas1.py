import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file to examine its content
file_path = 'phone_usage_india.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
print(data)

# Plotting the age distribution by phone brand
plt.figure(figsize=(10, 6))
colors = plt.cm.get_cmap('tab10', len(data['Phone Brand'].unique()))  # Get a color map
for i, brand in enumerate(data['Phone Brand'].unique()):
    plt.hist(data[data['Phone Brand'] == brand]['Age'].dropna(), 
             bins=20, edgecolor='k', alpha=0.7, label=brand, color=colors(i))

plt.title('Age Distribution by Phone Brand')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.legend(title='Phone Brand')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
