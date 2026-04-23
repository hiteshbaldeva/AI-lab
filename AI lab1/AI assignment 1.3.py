from collections import deque



graph = {
    "Raj": ["Sunil", "Neha_1"],
    "Sunil": ["Raj", "Akash", "Sneha", "Maya"],
    "Akash": ["Sunil", "Priya"],
    "Priya": ["Raj", "Aarav", "Akash"],
    "Neha_1": ["Raj", "Akash", "Sneha", "Aarav"],
    "Sneha": ["Sunil", "Neha_1", "Rahul"],
    "Maya": ["Rahul", "Arjun_1", "Sunil"],
    "Aarav": ["Neha_1", "Arjun_2"],
    "Neha_2": ["Priya", "Neha_1", "Rahul", "Arjun_2"],
    "Rahul": ["Neha_1", "Neha_2", "Sneha", "Maya", "Pooja", "Arjun_2"],
    "Arjun_1": ["Maya", "Pooja"],
    "Arjun_2": ["Aarav", "Neha_2", "Rahul"],
    "Pooja": ["Arjun_1", "Arjun_2", "Rahul"]
}


#  BFS Tree Construction

def bfs_tree(graph, start):
    visited = set([start])
    parent = {start: None}
    q = deque([start])

    while q:
        u = q.popleft()
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                parent[v] = u
                q.append(v)
    return parent


#  DFS Tree Construction

def dfs_tree(graph, start):
    visited = set()
    parent = {start: None}

    def dfs(u):
        visited.add(u)
        for v in graph.get(u, []):
            if v not in visited:
                parent[v] = u
                dfs(v)

    dfs(start)
    return parent




start_node = "Raj"   

bfs_parent = bfs_tree(graph, start_node)
dfs_parent = dfs_tree(graph, start_node)




print("BFS Tree edges:")
for child, parent in bfs_parent.items():
    if parent is not None:
        print(f"{parent} → {child}")

print("\nDFS Tree edges:")
for child, parent in dfs_parent.items():
    if parent is not None:
        print(f"{parent} → {child}")