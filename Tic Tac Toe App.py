'''
Brief outline of the steps involve in buildind the Tic Tac Toe game between two
# Player_1 name = Sani
# Player_2 name = Stev
# board
# display board
# play game
# handle turn
# check win
    # check rows
    # check columns
    # check diagonals
# check tie
# flip player
'''

# Declaring Global Variables
# game Board
board = ['----', '----', '----',
         '----', '----', '----',
         '----', '----', '----']

# If game is still going
game_still_going = True

# Win or tie
winner = None

# Current player
current_player = 'Sani'

# Game board display
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
# Function to allow playing of the game
def play_game():
    # dispaly game board (initial)
    display_board()

    # while game is still on
    while game_still_going:

        # handle single turn of an arbitrary player
        handle_turn(current_player)

        # check if the game is over
        check_if_game_over()

        # flip to other player
        flip_player()
    # Game ends
    if winner == 'Sani' or winner == 'Stev':
        print(winner + ' won.')
    elif winner == None:
        print('Tie')


# handle single turn of an arbitrary player
def handle_turn(player):

    print(player + '\'s turn')
    position = input('Choose a position from 1- 9: ')

    valid = False
    while not valid:
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input('invalid input. choose a position from 1-9: ')

        position = int(position) - 1

        if board[position] == '----':
            valid = True
        else:
            print('You can\'t go in there, that position is played already. Go again ' + player + '.')

    board[position] = player
    display_board()

# check if the game is over
def check_if_game_over():
    check_for_winner()
    check_if_tie()

# Check for winner
def check_for_winner():

    global winner
    # Check row
    row_winner = check_rows()
    # Check column
    column_winner = check_columns()
    # Check diagonal
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():
    global game_still_going
    #check if any of the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != '----'
    row_2 = board[3] == board[4] == board[5] != '----'
    row_3 = board[6] == board[7] == board[8] != '----'
    #If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return winner (X or 0)
    if row_1:
        return  board[0]
    elif row_2:
        return board[3]
    elif row_3:
       return board[6]
    return

def check_columns():
    global game_still_going
    # check if any of the rows have all the same value (and is not empty)
    column_1 = board[0] == board[3] == board[6] != '----'
    column_2 = board[1] == board[4] == board[7] != '----'
    column_3 = board[2] == board[5] == board[8] != '----'
    # If any row does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return winner (X or 0)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    global game_still_going
    # check if any of the rows have all the same value (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != '----'
    diagonal_2 = board[2] == board[4] == board[6] != '----'
    # If any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Return winner (X or 0)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return


def check_if_tie():
    global game_still_going
    if '----' not in board:
        game_still_going = False
    return

# flip to other player
def flip_player():
    global current_player
    # If the current_player is  X, change it to 0 and vice versa
    if current_player == 'Sani':
        current_player = 'Stev'
    elif current_player == 'Stev':
        current_player = 'Sani'
    return
play_game()