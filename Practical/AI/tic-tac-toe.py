import math
board = [' '] * 9
wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def print_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

def check_winner(player):
    return any(all(board[i] == player for i in pos) for pos in wins)

def is_draw():
    return ' ' not in board

def minimax(is_max):
    if check_winner('X'): return 1
    if check_winner('O'): return -1
    if is_draw(): return 0
    best = -math.inf if is_max else math.inf
    player = 'X' if is_max else 'O'
    for i in range(9):
        if board[i] == ' ':
            board[i] = player
            value = minimax(not is_max)
            board[i] = ' '
            best = max(best, value) if is_max else min(best, value)
    return best

def find_best_move():
    best_value, best_move = -math.inf, -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            value = minimax(False)
            board[i] = ' '
            if value > best_value:
                best_value, best_move = value, i
    return best_move

if input("\nEnter initial board state? (y/n): ").lower() == 'y':
    print("Use X, O or leave blank")
    for i in range(9):
        value = input(f"Position {i+1}: ").upper()
        board[i] = value if value in ['X', 'O'] else ' '

while True:
    print_board()
    if check_winner('X'):
        print("X wins!")
        break
    if check_winner('O'):
        print("O wins!")
        break
    if is_draw():
        print("Draw!")
        break

    move = int(input("Enter position (1-9): ")) - 1

    if move not in range(9):
        print("Invalid position!")
        continue
    if board[move] != ' ':
        print("Cell already occupied!")
        continue

    board[move] = 'O'

    if check_winner('O'):
        print_board()
        print("O wins!")
        break
    if is_draw():
        print_board()
        print("Draw!")
        break

    x_move = find_best_move()
    board[x_move] = 'X'
    print(f"X chooses position {x_move + 1}")

    if check_winner('X'):
        print_board()
        print("X wins!")
        break
    if is_draw():
        print_board()
        print("Draw!")
        break