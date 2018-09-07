#import os as os

# A simple Tic-Tac-Toe game app !
# Author: Gokul Reddy


def validate(board):
    """
    Validates whether the game is over
    :param board: The current state of the board
    :return: True if game is over, else False
    """

    if board[1] == board[2] == board[3] and board[1] != '#':
        return True
    if board[4] == board[5] == board[6] and board[4] != '#':
        return True
    if board[7] == board[8] == board[9] and board[7] != '#':
        return True
    if board[1] == board[4] == board[7] and board[4] != '#':
        return True
    if board[2] == board[5] == board[8] and board[2] != '#':
        return True
    if board[3] == board[6] == board[9] and board[3] != '#':
        return True
    if board[1] == board[5] == board[9] and board[1] != '#':
        return True
    if board[7] == board[5] == board[3] and board[7] != '#':
        return True
    return False


def print_the_board(board):
    """
    Prints the current board state !
    :param board: Current state of the board
    :return: Just prints it to console
    """

    # os.system('cls' if os.name == 'nt' else 'clear')
    print('    |    |    ')
    print('  {} |  {} | {} '.format(board[1], board[2], board[3]))
    print('    |    |    ')
    print('--------------')
    print('    |    |    ')
    print('  {} |  {} | {} '.format(board[4], board[5], board[6]))
    print('    |    |    ')
    print('--------------')
    print('    |    |    ')
    print('  {} |  {} | {} '.format(board[7], board[8], board[9]))
    print('    |    |    ')


def initialize_board():
    """
    Initializes a board for the game !
    :return: List which represents initial game setting
    """

    return ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']


def play_game():
    print('*************Welcome to Tic-Tac-Toe !*************')
    print('*************This is a 2 player game, Are u both ready !?*************')

    board = initialize_board()

    while True:
        choice1 = input('Player 1 - Pick your choice (X or O): ')
        if choice1 == 'X' or choice1 == 'O':
            break
        else:
            print('Oops !! Invalid choice, please try again !  ')
    if choice1 == 'X':
        choice2 = 'O'
    else:
        choice2 = 'X'

    print('*************Board has 9 cells, 3 rows and 3 columns!*************')
    print('*************Do remember the board is numbered from 1 to 9 starting from top left*************')

    for i in range(1, 11):
        print_the_board(board)
        res = validate(board)
        player = 1
        if i % 2 == 0:
            player = 2
        if res or i == 10:
            print('*************Game is over !*************')
            if i != 10:
                winner = 2
                if i % 2 == 0:
                    winner = 1
                print('$#$#$# Player {}, is the champion ! $#$#$#'.format(winner))
            else:
                print('$#$#$# It\'s a tie, lol ! $#$#$#')
            cont = input('Do u wanna play more !? :) (Y/n)')
            if cont.lower() == 'y':
                play_game()
            else:
                return
        while True:
            val = int(input('Player {}, what is your next position !?'.format(player)))
            if val < 1 or val > 9:
                print('************* Invalid position, try again ! *************')
            else:
                break

        if player == 1:
            board[val] = choice1
        else:
            board[val] = choice2


if __name__ == '__main__':
    play_game()


