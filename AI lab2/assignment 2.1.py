from collections import deque

def bfs_algo(start, goal):
    start = tuple(map(tuple, start))   #  map(function, iterable) applies a given function to each element of an iterable (like a list, tuple, or string).

    goal  = tuple(map(tuple, goal))
    count=1

    queue = deque([(start, [start])])   # (state, path)
    visited = set()
    visited.add(start)

    while queue:
        state, path = queue.popleft()

        if state == goal:
            print('EXPLORED STATE = ',count)
            return path

         
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    a, b = i, j

        moves = [(-1,0),(1,0),(0,-1),(0,1)]

        for dx, dy in moves:
            x, y = a+dx, b+dy
            if 0 <= x < 3 and 0 <= y < 3:
                new_state = [list(row) for row in state] #new_state = []  , for row in state:  ,new_state.append(list(row))

                new_state[a][b], new_state[x][y] = new_state[x][y], new_state[a][b]
                new_state = tuple(map(tuple, new_state))

                if new_state not in visited:
                    count=count+1
                    visited.add(new_state)
                    queue.append((new_state, path + [new_state]))
    
    return None

start=[ [7,2,4], [5,0,6], [8,3,1] ] 
goal=[ [1,2,3], [4,5,6], [7,8,0] ]
count=0
result = bfs_algo(start, goal)

print(result)