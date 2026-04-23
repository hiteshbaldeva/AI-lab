# Global counters
DLS_EXPLORED = 0
IDS_EXPLORED = 0

# Check if a state is valid
def is_valid(LG, LB, RG, RB):
    if LG > 0 and LB > LG:   
        return False
    if RG > 0 and RB > RG:  
        return False
    return True

# Generate successors
def successors(state):
    LG, LB, RG, RB, boat = state
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    next_states = []
    for g,b in moves:
        if boat == 'L':
            if LG >= g and LB >= b:
                new_state = (LG-g, LB-b, RG+g, RB+b, 'R')
                if is_valid(*new_state[:-1]):
                    next_states.append(new_state)
        else:  # boat on right
            if RG >= g and RB >= b:
                new_state = (LG+g, LB+b, RG-g, RB-b, 'L')
                if is_valid(*new_state[:-1]):
                    next_states.append(new_state)
    return next_states


def DLS(state, goal, limit, depth=0, path=[]):
    global DLS_EXPLORED
    DLS_EXPLORED += 1   # count every state explored

    path = path + [state]
    if state == goal:
        return path
    if depth == limit:
        return None
    for succ in successors(state):
        result = DLS(succ, goal, limit, depth+1, path)
        if result:
            return result
    return None

# Iterative Deepening Search with counter
def IDS(initial, goal):
    global IDS_EXPLORED, DLS_EXPLORED
    depth = 0
    while True:
        DLS_EXPLORED = 0  # reset for each depth run
        result = DLS(initial, goal, depth)
        IDS_EXPLORED += DLS_EXPLORED   # accumulate explored states
        if result:
            return result
        depth += 1

# Run
initial = (3,3,0,0,'L')
goal = (0,0,3,3,'R')

# DLS run
DLS_EXPLORED = 0
print("DLS with limit=3:", DLS(initial, goal, 3))
print("DLS explored states:", DLS_EXPLORED)

# IDS run
IDS_EXPLORED = 0
solution = IDS(initial, goal)
print("IDS solution:", solution)
print("IDS explored states:", IDS_EXPLORED)