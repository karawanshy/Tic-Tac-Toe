from random import randrange

'''
Initial State:
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   5   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
'''

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    
    print("+-------+-------+-------+")
    for i in range(3):
        print("|       |       |       |")
        for j in range(3):
            print(f"|   {board[i][j]}   ", end="")
        print("|\n|       |       |       |")
        print("+-------+-------+-------+")

def check_tie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                return False
    return True
 
def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.

    done = False
    while not done:
        cell = input("Please enter number of cell: ")
        if not cell.isdigit() or int(cell) < 1 or int(cell) > 9 :
            print("Invalid cell number!")
        else:
            for i in range(3):
                for j in range(3):
                    if board[i][j] == int(cell):
                        board[i][j] = 'O'
                        display_board(board)
                        done = True

                        if victory_for(board, 'O'):
                            print("You won!")
                            exit(1)
            if not done:
                print(f"Cell {cell} is already chosen!")


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    
    resultList = []
    
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'X' and board[i][j] != 'O': 
                resultList.append((i,j))
    
    return resultList


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game

    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return True
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return True
    
    return (board[0][2] == sign and board[1][1] == sign and board[2][0] == sign) or (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign)

def draw_move(board):
    # The function draws the computer's move and updates the board.

    freeCellsList = make_list_of_free_fields(board)
    length = len(freeCellsList)

    randomCell = freeCellsList[randrange(length)]

    board[randomCell[0]][randomCell[1]] = 'X'

    print("Computer's move: ")
    display_board(board)
    

def play_game():
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    while True:
        draw_move(board)

        if victory_for(board, 'X'):
            print("Computer won!")
            exit(1)
        elif check_tie(board):
            print("It's a tie")
            exit(1)
        
        enter_move(board)

play_game()
