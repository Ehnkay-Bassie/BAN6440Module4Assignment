import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

# Step 1: Load the dataset
file_path = 'jhu_csse_covid_19_timeseries_merged.csv'
covid_data = pd.read_csv(file_path)

# Step 2: Select relevant columns for clustering
features = covid_data[['confirmed', 'deaths', 'latitude', 'longitude']]

# Step 3: Handle missing values
imputer = SimpleImputer(strategy='mean')
features_imputed = imputer.fit_transform(features)

# Step 4: Normalize the data
scaler = StandardScaler()
features_normalized = scaler.fit_transform(features_imputed)

# Step 5: Use the Elbow Method to find the optimal number of clusters
inertia = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(features_normalized)
    inertia.append(kmeans.inertia_)

# Plot the Elbow Method results
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal Clusters')
plt.show()

# Step 6: Apply K-Means with optimal clusters (e.g., 3)
optimal_clusters = 3
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
covid_data['cluster'] = kmeans.fit_predict(features_normalized)

# Step 7: Display the first few rows with clusters
print(covid_data[['confirmed', 'deaths', 'latitude', 'longitude', 'cluster']].head())

# Save the clustered data to a new CSV file
covid_data.to_csv('covid_data_with_clusters.csv', index=False)