import kmeans
import random
import matplotlib.pyplot as plt


dataset = [(random.randint(0, 1000), random.randint(0, 1000)) for _ in range(200)]
k = 5
clustering, centroids = kmeans.lloyds_algorithm(dataset, k)
plt.plot([x[0] for x in dataset], [x[1] for x in dataset], 'ro')
plt.show()
