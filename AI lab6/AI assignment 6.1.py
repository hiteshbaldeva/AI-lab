
graph = [
    ("Chicago", "Detroit", 283),
    ("Chicago", "Cleveland", 345),
    ("Chicago", "Indianapolis", 182),
    ("Detroit", "Cleveland", 169),
    ("Detroit", "Buffalo", 256),
    ("Cleveland", "Pittsburgh", 134),
    ("Cleveland", "Columbus", 144),
    ("Cleveland", "Buffalo", 189),
    ("Indianapolis", "Columbus", 176),
    ("Pittsburgh", "Philadelphia", 305),
    ("Pittsburgh", "Baltimore", 247),
    ("Pittsburgh", "Buffalo", 215),
    ("Columbus", "Pittsburgh", 185),
    ("Buffalo", "Syracuse", 150),
    ("Syracuse", "New York", 254),
    ("Syracuse", "Boston", 312),
    ("Syracuse", "Philadelphia", 253),
    ("New York", "Philadelphia", 97),
    ("New York", "Boston", 215),
    ("New York", "Providence", 181),
    ("Philadelphia", "Baltimore", 101),
    ("Boston", "Providence", 50),
    ("Boston", "Portland", 107),
]

heuristic = {
    "Boston": 0, "Providence": 50, "Portland": 107, "New York": 215,
    "Philadelphia": 270, "Baltimore": 360, "Syracuse": 260, "Buffalo": 400,
    "Pittsburgh": 470, "Cleveland": 550, "Columbus": 640, "Detroit": 610,
    "Indianapolis": 780, "Chicago": 860
}


def get_neighbors(city):
    neighbors = []
    for u, v, w in graph:
        if u == city:
            neighbors.append((v, w))
        elif v == city: 
            neighbors.append((u, w))
    return neighbors


class PriorityQueue:
    def __init__(self):
        self.elements = []
    def empty(self):
        return len(self.elements) == 0
    def put(self, item, priority):
        self.elements.append((priority, item))
        self.elements.sort(key=lambda x: x[0])  
    def get(self):
        return self.elements.pop(0)[1]


def greedy_best_first(start, goal):
    frontier = PriorityQueue()
    frontier.put((start, [start], 0), heuristic[start])  # (city, path, cost)
    visited = set()
    while not frontier.empty():
        current, path, cost = frontier.get()
        if current == goal:
            return path, cost
        if current in visited:
            continue
        visited.add(current)
        for neighbor, edge_cost in get_neighbors(current):
            if neighbor not in visited:
                frontier.put((neighbor, path + [neighbor], cost + edge_cost), heuristic[neighbor])
    return None, None


def a_star(start, goal):
    frontier = PriorityQueue()
    frontier.put((start, [start], 0), heuristic[start])  # (city, path, g)
    visited = set()
    while not frontier.empty():
        current, path, g = frontier.get()
        if current == goal:
            return path, g
        if current in visited:
            continue
        visited.add(current)
        for neighbor, edge_cost in get_neighbors(current):
            if neighbor not in visited:
                g_new = g + edge_cost
                f_new = g_new + heuristic[neighbor]
                frontier.put((neighbor, path + [neighbor], g_new), f_new)
    return None, None

# Run both searches from Chicago to Boston
gbfs_path, gbfs_cost = greedy_best_first("Chicago", "Boston")
astar_path, astar_cost = a_star("Chicago", "Boston")

print("GBFS path:", gbfs_path, "Total cost:", gbfs_cost)
print("A* path:", astar_path, "Total cost:", astar_cost)