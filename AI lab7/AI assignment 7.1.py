import random


def heuristic(board):
    h = 0
    n = len(board)
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j]:  # same row
                h += 1
            if abs(board[i] - board[j]) == abs(i - j):  
                h += 1
    return h


def random_board(n=8):
    return [random.randint(0, n-1) for _ in range(n)]           #[0,1,2,3,5,7,4,1]

# Steepest-ascent hill climbing
def hill_climb(board):
    steps = 0
    current_h = heuristic(board)
    n = len(board)

    while True:
        best_h = current_h
        best_board = board[:]

        # Try moving each queen in its column
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
            # No improvement → local minimum
            break

    return current_h, steps, (current_h == 0)


results = []
for trial in range(1, 51):
    board = random_board()
    init_h = heuristic(board)
    final_h, steps, solved = hill_climb(board)
    results.append((trial, init_h, final_h, steps, "Solved" if solved else "Fail"))


print(f"{'Trial':<6}{'Initial h':<10}{'Final h':<10}{'Steps':<8}{'Status':<8}")
for r in results:
    print(f"{r[0]:<6}{r[1]:<10}{r[2]:<10}{r[3]:<8}{r[4]:<8}")