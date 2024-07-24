from pyclustering.cluster.dbscan import dbscan
from pyclustering.cluster import cluster_visualizer
from pyclustering.utils import read_sample
from pyclustering.samples.definitions import FCPS_SAMPLES
 
# Sample for cluster analysis.
# sample = read_sample(FCPS_SAMPLES.SAMPLE_CHAINLINK)

sample = [[35.223736, 139.717529],[35.223747, 139.717606],[35.223759, 139.717743],[35.223763, 139.717819],[35.223763, 139.71785],[35.223763, 139.717941], [35.223763, 139.717941], [35.223763, 139.718033], [35.223743, 139.718246], [35.223736, 139.718292], [60.026218,22.03404],
          [80.669998, 72.034042], [80.669998,72.034042], [60.026218, 22.03404], [80.669998, 72.034042], [60.026218, 22.03404], [0,0]]

print(sample) 

# Create DBSCAN algorithm.
dbscan_instance = dbscan(sample, 0.2, 1)
 
# Start processing by DBSCAN.
dbscan_instance.process()
 
# Obtain results of clustering.
clusters = dbscan_instance.get_clusters()
noise = dbscan_instance.get_noise()
cluster_encoding = dbscan_instance.get_cluster_encoding()

# Visualize clustering results
visualizer = cluster_visualizer()
visualizer.append_clusters(clusters, sample)
visualizer.append_cluster(noise, sample, marker='x')
visualizer.save("visualization.jpg")

print(clusters)
print(noise)
