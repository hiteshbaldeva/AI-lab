import math

player = 'X'   # AI (MAX)
opponent = 'O' # Human (MIN)

# Print board
def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], board[i+1], board[i+2])
    print()



wins = [
    [0,1,2], [3,4,5], [6,7,8],  # rows
    [0,3,6], [1,4,7], [2,5,8],  # cols
    [0,4,8], [2,4,6]            # diagonals
]

# Evaluate board
def evaluate(board):
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] and board[w[0]] != '_':
            return 10 if board[w[0]] == player else -10
    return 0


def is_moves_left(board):
    return '_' in board


# 🔥 Alpha-Beta Minimax
def minimax(board, depth, is_max, alpha, beta):
    score = evaluate(board)

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf

        for i in range(9):
            if board[i] == '_':
                board[i] = player

                val = minimax(board, depth+1, False, alpha, beta)
                best = max(best, val)

                board[i] = '_'
                alpha = max(alpha, best)

                #  Pruning
                if beta <= alpha:
                    return best

        return best

    else:
        best = math.inf

        for i in range(9):
            if board[i] == '_':
                board[i] = opponent

                val = minimax(board, depth+1, True, alpha, beta)
                best = min(best, val)

                board[i] = '_'
                beta = min(beta, best)

                # ✂️ Pruning
                if beta <= alpha:
                    return best

        return best


# Find best move
def find_best_move(board):
    best_val = -math.inf
    best_move = -1

    for i in range(9):
        if board[i] == '_':
            board[i] = player

            move_val = minimax(board, 0, False, -math.inf, math.inf)

            board[i] = '_'

            if move_val > best_val:
                best_val = move_val
                best_move = i

    return best_move


#  Game Loop
def play_game():
    board = ['_'] * 9

    print("Positions are:")
    print("0 1 2\n3 4 5\n6 7 8\n")

    print("You are O, AI is X\n")

    while True:
        print_board(board)

        # Human move
        move = int(input("Enter position (0-8): "))
        if move < 0 or move > 8 or board[move] != '_':
            print("Invalid move! Try again.")
            continue

        board[move] = opponent

        if evaluate(board) == -10:
            print_board(board)
            print("You win!")
            break
        if not is_moves_left(board):
            print_board(board)
            print("Draw!")
            break

        # AI move
        ai_move = find_best_move(board)
        board[ai_move] = player

        print(f"AI plays at position {ai_move}")

        if evaluate(board) == 10:
            print_board(board)
            print("AI wins!")
            break
        if not is_moves_left(board):
            print_board(board)
            print("Draw!")
            break


# Run game
play_game()