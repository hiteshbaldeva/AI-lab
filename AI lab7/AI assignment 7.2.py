import random, math


def heuristic(board):
    h = 0
    n = len(board)
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j]: 
                h += 1
            if abs(board[i] - board[j]) == abs(i - j):  
                h += 1
    return h


def random_board(n=8):
    return [random.randint(0, n-1) for _ in range(n)]

# Steepest-ascent hill climbing
def steepest_ascent(board):
    steps = 0
    current_h = heuristic(board)
    n = len(board)

    while True:
        best_h = current_h
        best_board = board[:]

        for col in range(n):
            for row in range(n):
                if row != board[col]:
                    new_board = board[:]
                    new_board[col] = row
                    h = heuristic(new_board)
                    if h < best_h:
                        best_h = h
                        best_board = new_board

        if best_h < current_h:
            board = best_board
            current_h = best_h
            steps += 1
        else:
            break

    return current_h, steps, (current_h == 0)

# First-choice hill climbing
def first_choice(board):
    steps = 0
    current_h = heuristic(board)
    n = len(board)

    while True:
        improved = False
        for col in range(n):
            for row in range(n):
                if row != board[col]:
                    new_board = board[:]
                    new_board[col] = row
                    h = heuristic(new_board)
                    if h < current_h:
                        board = new_board
                        current_h = h
                        steps += 1
                        improved = True
                        break
            if improved:
                break
        if not improved:
            break

    return current_h, steps, (current_h == 0)

# Random-restart hill climbing
def random_restart(max_restarts=50):
    total_steps = 0
    for _ in range(max_restarts):
        board = random_board()
        final_h, steps, solved = steepest_ascent(board)
        total_steps += steps
        if solved:
            return final_h, total_steps, True
    return final_h, total_steps, False

# Simulated annealing (select the bad position so that it can improve later)
def simulated_annealing(board, max_steps=1000, start_temp=30.0, cooling=0.95):
    steps = 0
    current_h = heuristic(board)
    n = len(board)
    temp = start_temp

    while steps < max_steps and current_h > 0:
        col = random.randint(0, n-1)
        row = random.randint(0, n-1)
        new_board = board[:]
        new_board[col] = row
        new_h = heuristic(new_board)

        delta = new_h - current_h
        if delta < 0 or random.random() < math.exp(-delta / temp):
            board = new_board
            current_h = new_h
        temp *= cooling
        steps += 1

    return current_h, steps, (current_h == 0)


def run_experiment(trials=50):
    print(f"{'Trial':<6}{'Algorithm':<15}{'Initial h':<10}{'Final h':<10}{'Steps':<8}{'Status':<8}")
    for trial in range(1, trials+1):
        board = random_board()
        init_h = heuristic(board)

        
        final_h, steps, solved = steepest_ascent(board[:])
        print(f"{trial:<6}{'Steepest':<15}{init_h:<10}{final_h:<10}{steps:<8}{'Solved' if solved else 'Fail':<8}")

        
        final_h, steps, solved = first_choice(board[:])
        print(f"{trial:<6}{'First-choice':<15}{init_h:<10}{final_h:<10}{steps:<8}{'Solved' if solved else 'Fail':<8}")

       
        final_h, steps, solved = random_restart()
        print(f"{trial:<6}{'Random-restart':<15}{init_h:<10}{final_h:<10}{steps:<8}{'Solved' if solved else 'Fail':<8}")

        
        final_h, steps, solved = simulated_annealing(board[:])
        print(f"{trial:<6}{'SimAnneal':<15}{init_h:<10}{final_h:<10}{steps:<8}{'Solved' if solved else 'Fail':<8}")

# Run 50 trials
run_experiment(50)