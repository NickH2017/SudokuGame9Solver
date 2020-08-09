from boards import Easy
import sys

sys.setrecursionlimit(10000)

#
# Python Solvable Sudoku Game (Text)
#

# Prints the 9 x 9 sudoku board
def printBoard(arr):
    
    for row in range(len(arr)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - -")

        for col in range(len(arr[row])):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")

            if col == 8:
                print(arr[row][col])
            else:
                print(str(arr[row][col]) + " ", end="")

#
# Finds out if the cell is valid based on row, col, and 3x3 square sudoku rules
#
def isValid(board, num, loc):

    # Checks the row

    for col in range(len(board[0])):
        if num == board[loc[0]][col] and loc[1] != col:
            #print("Number is in the Row")
            return False

    # Checks the col

    for row in range(len(board)):
        if num == board[row][loc[1]] and loc[0] != row:
            #print("Number is in the Col")
            return False

    # Checks the 3x3 square
    box_x = loc[0] // 3
    box_y = loc[1] // 3

    if box_x == 0:
        range_x = [0,1,2]
    elif box_x == 1:
        range_x = [3,4,5]
    else:
        range_x = [6,7,8]

    if box_y == 0:
        range_y = [0,1,2]
    elif box_y == 1:
        range_y = [3,4,5]
    else:
        range_y = [6,7,8]

    for row in range_x:
        for col in range_y:
            if num == board[row][col] and (row,col) != loc:
                #print("number already in 3x3")
                return False

    return True

#
# Returns True if cell is empty
#
def isEmpty(cell):

    if cell == 0:
        return True
    else:
        return False

#
# Finds the next empty cell in the sudoku board
#
def find_empty(arr):

    for row in range(len(arr)):
        for col in range(len(arr[0])):      
            cell = arr[row][col]
            if isEmpty(cell):
                return [row, col]

    return None
#
# Solves the board
#
def solve(arr):

    location = [0,0]
   

    # Stores the row col cordinates to help backtracking algorithm retrace last location 
    location = find_empty(arr)

    if not location:
        return True

    row, col = location

    for num in range(1,10):

        if isValid(arr, num, location):
            arr[row][col] = num

            if solve(arr):
                return True

            arr[row][col] = 0

    #return False



                



solve(Easy)
printBoard(Easy)

    