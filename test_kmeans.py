import unittest
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

class TestKMeansClustering(unittest.TestCase):

    def setUp(self):
        # Load the dataset and preprocess it for testing
        file_path = 'jhu_csse_covid_19_timeseries_merged.csv'
        self.data = pd.read_csv(file_path)
        features = self.data[['confirmed', 'deaths', 'latitude', 'longitude']]
        imputer = SimpleImputer(strategy='mean')
        features_imputed = imputer.fit_transform(features)
        scaler = StandardScaler()
        self.features_normalized = scaler.fit_transform(features_imputed)

    def test_kmeans_clusters(self):
        # Test if KMeans clusters without errors
        kmeans = KMeans(n_clusters=3, random_state=42)
        clusters = kmeans.fit_predict(self.features_normalized)
        self.assertEqual(len(set(clusters)), 3)

    def test_output_format(self):
        # Ensure that the clustered data has the correct number of columns
        kmeans = KMeans(n_clusters=3, random_state=42)
        self.data['cluster'] = kmeans.fit_predict(self.features_normalized)
        self.assertIn('cluster', self.data.columns)

if __name__ == '__main__':
    unittest.main()