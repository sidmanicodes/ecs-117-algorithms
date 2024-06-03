import numpy as np
from numpy.typing import NDArray
from typing import List

def agglomerative_clustering(data: NDArray) -> List[List[NDArray]]:
    """
    Python implementation of the agglomerative clustering algorithm, 
    a bottom-up approach to hierarchical clustering

    NOTE: THIS FUNCTION IS NOT FULLY IMPLEMENTED, IT WILL NOT RUN ... unless
    someone forks this repo and makes it work :)

    Arguments:
        - data (NDArray): data points

    Returns:
        - clusters (NDArray): cluster assignments
    """
    n = len(data)
    clusters = [[i] for i in range(n)]

    dist_matrix = compute_dist_matrix(clusters)

    while len(clusters) > 1:
        # Find the closest clusters
        c1, c2 = find_closest_clusters(dist_matrix)

        # Merge the clusters
        clusters[c1].extend(clusters[c2])
        clusters.pop(c2)

        # Recompute the distance matrix with the new clustering
        dist_matrix = compute_dist_matrix(dist_matrix)

        print(f"Merged clusters {c1} and {c2} into {clusters[c1]}")

    return clusters

data = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [8, 8],
    [8, 5],
    [7, 2]
])