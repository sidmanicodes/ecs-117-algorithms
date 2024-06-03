import math
import random as rand
import string
from pprint import pformat
from typing import List, Tuple, Dict

def k_means(k: int, data: List[Tuple[int]], iteration_limit: int = 10) -> Dict[str, List[Tuple[int, int]]]:
    # Get mins and maxes of x and y coordinates
    x_min = min([x for x, _ in data])
    x_max = max([x for x, _ in data])
    y_min = min([y for _, y in data])
    y_max = max([y for _, y in data])

    # Create initial clusters
    alphabet = list(string.ascii_uppercase)
    clusters = {}
    centroids = {}
    centroid_table = {} # Used to keep track of previous centroids
    for i in range(k):
        name = alphabet[i]
        clusters[name] = []

        initial_x = rand.randint(x_min, x_max)
        initial_y = rand.randint(y_min, y_max)

        centroids[name] = [initial_x, initial_y]
        centroid_table[name] = [(initial_x, initial_y)]


    print({'Initial cetroids: ': centroids})

    # Assign points to clusters until iteration limit is reached
    for i in range(iteration_limit):
        # Clear cluster assignments
        for name, _ in clusters.items():
            clusters[name] = []

        # Iterate over all data points
        for x, y in data:
            distances = {} # This is to hold the distances to each cluster
            
            # For every cluster location, get the distance from the point to
            # the cluster
            for name, (x_c, y_c) in centroids.items():
                dist = math.sqrt((x-x_c)**2 + (y-y_c)**2)
                distances[name] = dist
                
            # Assign the point to a cluster based on the smallest distance
            chosen_cluster = [name for name, _ in sorted(distances.items(), key=lambda x: x[1], reverse=True)][0]
            clusters[chosen_cluster].append([x, y])

        # Recalculate the centroid location
        for name, assignments in clusters.items():
            # Calculate the x and y means of the new cluster assignments
            # This will eventually minimize the distance between the data and the centroids
            x_mean = sum([x for x, _ in assignments]) / (len(assignments) if assignments else 1)
            y_mean = sum([y for _, y in assignments]) / (len(assignments) if assignments else 1)

            centroids[name] = [x_mean, y_mean]
            centroid_table[name].append((x_mean, y_mean))

        # Check to see if the centroid location stayed the same from the previous iteration
        stayed_same = []
        for name in centroids.keys():
            # If the centroid location stayed the same, note this in stayed_same array
            if i > 0 and [*centroids[name]] == [*centroid_table[name][i-1]]:
                stayed_same.append(True)

            # Else, append false
            else:
                stayed_same.append(False)

        # If all centroids stayed the same, exit early
        if all(stayed_same):
            print(f"Clusters stopped changing at iteration {i+1}")
            for name in centroids.keys():
                print(pformat({"Previous centroids: ": centroid_table[name][i-1]}))
            break

    return pformat({'Clusters': clusters, 'Centroids': centroids})

k = 2
data = [(1, 8), (2, 6), (3, 9), (4, 5)]
iteration_limit = 5

print(k_means(k=k, data=data, iteration_limit=iteration_limit))