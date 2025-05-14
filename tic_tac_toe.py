# Library to color the text (X and O)
from termcolor import colored

# constants for the players
X = 'X'
O = 'O'

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# color the X in red and O in blue using termcolor
def cell(mark):
    color = 'red' if mark == X else 'blue'
    return colored(mark, color)

# print current board state
def print_board(board):
    line = '---+---+---'
    print(line)
    for row in board:
        print(f'{cell(row[0])} | {cell(row[1])} | {cell(row[2])}')
        print(line)

def check_winner(board):
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True

    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]  != ' ':
            return True

    # check diagonals
    if  board[0][0] == board[1][1] == board[2][2] != ' ' or \
        board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False

# returns True if the board is full.
def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# Prompts the user to enter a valid row or column index (0-2).
# Handles invalid input using a try-except block.
def get_position(prompt):
    while True:
        try:
            position = int(input(prompt))
            if position < 0 or position > 2:
                raise ValueError
            return position
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 2.")

def get_move(current_player):
    print(f"Player {current_player}'s turn")
    while True:
        # Get row and column from the user
        row = get_position("Enter row (0-2): ")
        col = get_position("Enter column (0-2): ")

        if board[row][col] == ' ':
            board[row][col] = current_player
            break
        else:
            print("Cell already taken! Try again.")

def play():
    print_board(board)
    current_player = X

    while True:
        get_move(current_player)
        print_board(board)

        if check_winner(board):
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        # Switch players
        current_player = O if current_player == X else X

play()
