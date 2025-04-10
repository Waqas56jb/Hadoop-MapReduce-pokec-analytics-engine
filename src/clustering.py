from mrjob.job import MRJob
import numpy as np
from sklearn.cluster import KMeans

class MRKMeans(MRJob):
    def mapper(self, _, line):
        if "user_id" in line:
            return
        fields = line.split(',')
        age = float(fields[2])
        completion = float(fields[4])
        yield None, (age, completion)

    def reducer(self, _, values):
        data = list(values)
        X = np.array(data)
        kmeans = KMeans(n_clusters=3)
        kmeans.fit(X)
        yield "Cluster Centers", kmeans.cluster_centers_.tolist()

if __name__ == '__main__':
    MRKMeans.run()