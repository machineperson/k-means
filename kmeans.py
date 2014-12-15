import math
import random 

def lloyds_algorithm(dataset, k):
    """ Given a list of points and a number k of desired clusters,
    groups the points into k clusters. Returns a dictionary with points as keys
    and the centroid of their assigned cluster as values, and a set of centroids."""
    # assign initial centroids randomly
    centroids = random.sample(dataset, k)
    clusters = {}
    while True: # we could add a maximum amount of iterations here
        new_clusters = update_clusters(centroids, dataset)
        new_centroids = update_centroids(new_clusters)
        # check if clusters and centroids haven't changed
        # (<= is a set comparison here)
        if(new_centroids <= centroids and centroids <= new_centroids 
                and equal(new_clusters, clusters)):
            return new_clusters, new_centroids
        else:
            clusters = new_clusters
            centroids = new_centroids

def update_centroids(cluster_labeling):
    """ Given a labeling of the dataset that assigns each point to a cluster, 
    returns a set of k centroids."""
    centroids = set() 
    for centroid in cluster_labeling.values():
        cluster = []
        for point in cluster_labeling.keys():
            if cluster_labeling[point] == centroid:
                cluster.append(point)
        # compute the mean of all points in a cluster
        point_sum = []
        for point in cluster:
            point_sum = [(point_sum[i] if len(point_sum) > 0 else 0)
                    + point[i] for i in range(len(list(point)))]
        # we need the conversion into a tuple so the points can be dict keys
        centroids.add(tuple([x_n / len(cluster) for x_n in point_sum]))
    return centroids

def update_clusters(centroids, dataset):
    """ Given a set of k centroids and a dataset, returns k clusters to contain the points
    closest in distance to each centroid """
    return {x: closest_centroid(x, centroids) for x in dataset}

def closest_centroid(point, centroids):
    """ Given a point and a set of centroids, returns the centroid
    closest to the given point"""
    minimum_distance = None
    closest = None
    for c in centroids:
        if minimum_distance is None or minimum_distance > distance(point, c):
            minimum_distance = distance(point, c)
            closest = c
    return closest

def distance(x, y):
    """ Returns the Euclidean distance between two points given as tuples """
    lx = list(x)
    ly = list(y)
    return math.sqrt(sum([(lx[n] - ly[n])**2 for n in range(len(lx))]))

def equal(d1, d2):
    """ Returns True if dictionaries d1 and d2 contain the same keys and assign the same value
    to each key, False otherwise"""
    for key, value in d1.iteritems():
        if key not in d2 or d2[key] != value:
            return False
    return len([x for x in d2.keys() if x not in d1]) == 0

