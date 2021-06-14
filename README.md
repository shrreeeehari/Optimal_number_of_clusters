# Optimal_number_of_clusters

Performance comparison of various techniques for determining the optimal number of clusters in a data set .

![](images/cluster.jpg)

We have used 6 clustering methods:
1.Elbow Method

2.Average Silhouette Method

3.Gap Statistics Method

4.Davies-Bouldin Index

5.Calinski-Harabasz Index

6.Dendrogram

The above techniques have been tested over open source available datasets imported using sklearn library which are:
Datasets used:

1.Boston

2.Iris

3.Digits

Elbow Method

It calculates the Within-Cluster-Sum of Squared Errors (WSS) for different values of k, choose the k for which WSS first starts to diminish. 

Optimal Cluster - Cluster K after which there is negligible changes to the clustering.

Average Silhouette Method

The silhouette value measures how similar a point is to its own cluster (cohesion) compared to other clusters (separation). 

Optimal Cluster - Cluster K with the highest peak (average silhouette score)

Gap Statistics Method

Compares the total within intra-cluster variation [wss] for different values of k with their expected values under null reference distribution of the data.
The estimate of the optimal clusters will be value that maximize the gap statistic.

Optimal Cluster - Cluster K with the max gap statistic

Davies-Bouldin Index

Evaluates intra-cluster similarity and inter-cluster differences.
If two clusters are close together but have a large spread then this ratio will
be large, indicating that these clusters are not very distinct.

Optimal Cluster - Cluster K with the least DBI



