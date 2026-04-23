import pandas as pd
import numpy as np

# -----------------------------
# STEP 1: LOAD DATA
# -----------------------------
data = pd.read_csv("C:/Users/Hitesh m/Downloads/cities.csv", sep=r'\s+')
points = data.values

# -----------------------------
# STEP 2: INITIALIZE CENTERS
# -----------------------------
k = 3
np.random.seed(42)
centers = points[np.random.choice(len(points), k, replace=False)]

# -----------------------------
# STEP 3: ASSIGN CLUSTERS
# -----------------------------
def assign_clusters(points, centers):
    clusters = [[] for _ in range(len(centers))]

    for p in points:
        distances = [np.sum((p - c)**2) for c in centers]
        idx = np.argmin(distances)
        clusters[idx].append(p)

    return clusters

# -----------------------------
# STEP 4: UPDATE CENTERS
# -----------------------------
def update_centers(clusters):
    new_centers = []

    for cluster in clusters:
        if len(cluster) == 0:
            new_centers.append(np.random.rand(2))
        else:
            new_centers.append(np.mean(cluster, axis=0))

    return np.array(new_centers)

# -----------------------------
# STEP 5: COST FUNCTION
# -----------------------------
def compute_cost(clusters, centers):
    cost = 0
    for i, cluster in enumerate(clusters):
        for p in cluster:
            cost += np.sum((p - centers[i])**2)
    return cost

# -----------------------------
# STEP 6: MAIN LOOP WITH OUTPUT
# -----------------------------
max_iter = 100
prev_cost = float('inf')

print("\n--- K-Means Iteration Process ---\n")

for i in range(max_iter):
    clusters = assign_clusters(points, centers)
    new_centers = update_centers(clusters)
    cost = compute_cost(clusters, new_centers)

    # Print only first few iterations + final
    if i < 5 or abs(prev_cost - cost) < 1e-3:
        print(f"\nIteration {i+1}")
        print("Centers:")
        print(new_centers)

        print("Cluster Sizes:", [len(c) for c in clusters])

        print(f"Cost: {cost:.2f}")

        if prev_cost != float('inf'):
            print(f"Cost Decreased By: {prev_cost - cost:.2f}")

    # Check convergence
    if np.allclose(centers, new_centers):
        print(f"\n✅ Converged at iteration {i+1}")
        centers = new_centers
        break

    centers = new_centers
    prev_cost = cost

# -----------------------------
# STEP 7: FINAL OUTPUT
# -----------------------------
final_cost = compute_cost(clusters, centers)

print("\n--- FINAL RESULT ---")
print("Final Airport Locations:")
print(centers)

print(f"\nFinal Cost: {final_cost:.2f}")