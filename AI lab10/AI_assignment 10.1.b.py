import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# LOAD DATA
# -----------------------------
data = pd.read_csv("C:/Users/Hitesh m/Downloads/cities.csv", sep=r'\s+')
points = data.values

# -----------------------------
# ASSIGN CLUSTERS
# -----------------------------
def assign_clusters(points, centers):
    clusters = [[] for _ in range(len(centers))]

    for p in points:
        distances = [np.sum((p - c)**2) for c in centers]
        idx = np.argmin(distances)
        clusters[idx].append(p)

    return clusters

# -----------------------------
# COST FUNCTION
# -----------------------------
def compute_cost(clusters, centers):
    cost = 0
    for i, cluster in enumerate(clusters):
        for p in cluster:
            cost += np.sum((p - centers[i])**2)
    return cost

# -----------------------------
# GRADIENT FUNCTION (KEY PART 🔥)
# -----------------------------
def compute_gradient(cluster, center):
    grad = np.zeros_like(center)

    for p in cluster:
        grad += (center - p)   # derivative of (p - center)^2

    return 2 * grad


# -----------------------------
# NEWTON / GRADIENT METHOD
# -----------------------------
def newton_method(points, k=3, max_iter=50, alpha=0.1):
    np.random.seed(42)
    centers = points[np.random.choice(len(points), k, replace=False)]

    print("\n--- Newton Method Iterations ---\n")

    for i in range(max_iter):
        clusters = assign_clusters(points, centers)

        new_centers = []

        for idx, cluster in enumerate(clusters):

            if len(cluster) == 0:
                new_centers.append(np.random.rand(2))
                continue

            center = centers[idx]

            #  Compute gradient
            grad = compute_gradient(cluster, center)

            #  Update using gradient (like Newton/optimization step)
            new_center = center - alpha * grad / len(cluster)

            new_centers.append(new_center)

        new_centers = np.array(new_centers)

        cost = compute_cost(clusters, new_centers)

        print(f"Iteration {i+1}")
        print("Centers:\n", new_centers)
        print(f"Cost: {cost:.2f}\n")

        if np.allclose(centers, new_centers, atol=1e-3):
            print(f"✅ Converged at iteration {i+1}")
            break

        centers = new_centers

    return centers, clusters


# -----------------------------
# RUN
# -----------------------------
centers, clusters = newton_method(points)

# -----------------------------
# FINAL OUTPUT
# -----------------------------
print("\nFinal Centers:")
print(centers)

# -----------------------------
# PLOT
# -----------------------------
for i, cluster in enumerate(clusters):
    cluster = np.array(cluster)
    plt.scatter(cluster[:,0], cluster[:,1], label=f"Cluster {i+1}")

plt.scatter(centers[:,0], centers[:,1], marker='X', s=200, label='Centers')
plt.legend()
plt.title("Newton/Gradient Based Clustering")
plt.show()