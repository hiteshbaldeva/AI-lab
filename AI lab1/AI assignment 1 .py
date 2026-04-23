def dfs_all_costs(graph, current, goal, path=None, cost=0, results=None):
    if path is None:
        path = [current]
    if results is None:
        results = []

    if current == goal:
        results.append((path, cost))
        return results

    for neighbor, step_cost in graph[current].items():  
        if neighbor not in path: 
            dfs_all_costs(graph, neighbor, goal, path + [neighbor], cost + step_cost, results)
    return results

graph = {
    "Chicago": {"Detroit": 283, "Cleveland": 345, "Indianapolis": 182},
    "Detroit": {"Chicago": 283, "Cleveland": 169, "Buffalo": 256},
    "Cleveland": {"Detroit": 169, "Pittsburgh": 134, "Columbus": 144, "Chicago": 345, "Buffalo": 189},
    "Columbus": {"Cleveland": 144, "Indianapolis": 176, "Pittsburgh": 185},
    "Indianapolis": {"Chicago": 182, "Columbus": 176},
    "Pittsburgh": {"Cleveland": 134, "Buffalo": 215, "Philadelphia": 305, "Columbus": 185, "Baltimore": 247},
    "Buffalo": {"Detroit": 256, "Pittsburgh": 215, "Syracuse": 150, "Cleveland": 189},
    "Syracuse": {"Buffalo": 150, "New York": 254, "Boston": 312, "Philadelphia": 253},
    "New York": {"Syracuse": 254, "Philadelphia": 97, "Boston": 215, "Providence": 181},
    "Philadelphia": {"New York": 97, "Pittsburgh": 305, "Baltimore": 101, "Syracuse": 253},
    "Baltimore": {"Philadelphia": 101,"Pittsburgh":247}, 
    "Boston": {"Syracuse": 312, "Providence": 50, "New York": 215, "Portland": 107},
    "Providence": {"Boston": 50, "New York": 181},
    "Portland": {"Boston": 107}
}

# Run DFS
dfs_results = dfs_all_costs(graph, "Syracuse", "Chicago")
count=0
print("\nDFS Paths & Costs:")
for path, cost in dfs_results:
    print(path, "=>", cost)
    count=count+1
print(count)
