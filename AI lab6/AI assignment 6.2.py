maze = [
    [2, 0, 0, 0, 1],
    [0, 1, 0, 0, 3],
    [0, 3, 0, 1, 1],
    [0, 1, 0, 0, 1],
    [3, 0, 0, 0, 3]
]

ROWS, COLS = len(maze), len(maze[0])

# Find start and rewards
start = None
rewards = []
for i in range(ROWS):
    for j in range(COLS):
        if maze[i][j] == 2:
            start = (i, j)
        elif maze[i][j] == 3:
            rewards.append((i, j))

# Manhattan heuristic
def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def get_neighbors(pos):
    x, y = pos
    moves = [(0,1),(0,-1),(1,0),(-1,0)]
    result = []
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < ROWS and 0 <= ny < COLS and maze[nx][ny] != 1:
            result.append((nx, ny))
    return result

# Custom Priority Queue
class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def push(self, item):
        self.queue.append(item)
        self.queue.sort(key=lambda x: x[0])  # sort by f value
    
    def pop(self):
        return self.queue.pop(0)  # smallest f comes first
    
    def empty(self):
        return len(self.queue) == 0

# A* search from one point to one goal
def a_star(start, goal):
    frontier = PriorityQueue()
    frontier.push((heuristic(start, goal), 0, start, [start]))
    visited = set()
    while not frontier.empty():
        f, g, current, path = frontier.pop()
        if current == goal:
            return path, g
        if current in visited:
            continue
        visited.add(current)
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                g_new = g + 1
                f_new = g_new + heuristic(neighbor, goal)
                frontier.push((f_new, g_new, neighbor, path+[neighbor]))
    return None, None

current = start
visited_tiles = [start]
total_cost = 0

for reward in rewards:
    path, cost = a_star(current, reward)
    if path:
        visited_tiles.extend(path[1:])  # avoid duplicating current
        total_cost += cost
        current = reward

print("Visited tiles:", visited_tiles)
print("Total cost:", total_cost)