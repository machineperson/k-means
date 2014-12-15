import kmeans
import random
import matplotlib.pyplot as plt


dataset = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(20)] + \
[(random.randint(100, 200), random.randint(100, 200)) for _ in range(20)] + \
[(random.randint(200, 300), random.randint(200, 300)) for _ in range(20)] + \
[(random.randint(300, 400), random.randint(300, 400)) for _ in range(20)] + \
[(random.randint(400, 500), random.randint(400, 500)) for _ in range(20)]

k = 5
clustering, centroids = kmeans.lloyds_algorithm(dataset, k)
plt.plot([x[0] for x in dataset], [x[1] for x in dataset], 'ro', [c[0] for c in centroids], [c[1] for c in centroids], 'bo')
plt.show()
