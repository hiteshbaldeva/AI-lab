import math


def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        print("---------")

# Check winner
def check_winner(board):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != " ":
            return board[pos[0]]
    return None

# Check draw
def is_draw(board):
    return " " not in board

# Minimax algorithm
def minimax(board, is_max):
    winner = check_winner(board)

    if winner == "X":
        return 1
    if winner == "O":
        return -1
    if is_draw(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, False)
                board[i] = " "
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, True)
                board[i] = " "
                best = min(best, score)
        return best

# Find best move for AI
def best_move(board):
    best_score = math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, True)
            board[i] = " "

            if score < best_score:
                best_score = score
                move = i

    return move

# Main game
def play_game():
    board = [" "] * 9

    print("You are X, Computer is O")
    
    while True:
        print_board(board)

        # Human move
        move = int(input("Enter your move (0-8): "))
        if board[move] != " ":
            print("Invalid move! Try again.")
            continue

        board[move] = "X"

        if check_winner(board) == "X":
            print_board(board)
            print("You win!")
            break

        if is_draw(board):
            print_board(board)
            print("Draw!")
            break

        # Computer move
        print("Computer is thinking...")
        ai_move = best_move(board)
        board[ai_move] = "O"

        if check_winner(board) == "O":
            print_board(board)
            print("Computer wins!")
            break

        if is_draw(board):
            print_board(board)
            print("Draw!")
            break


# Run game
play_game()