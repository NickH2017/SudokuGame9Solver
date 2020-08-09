#import pygame
from solver import printBoard
from boards import Easy
from boards import Medium

#
# UI that will test the boards "Text based UI"
#

if __name__ == "__main__":

    print("Welcome to Sudoku!\n\n")
    userinput = -1
    while userinput != "q":

        print("\nNew Game\n")
        print("Continue")
        userinput = input("Enter cmd:")

        if userinput == "n":
            while userinput != "b":
                print("Easy")
                print("Medium")
                print("Hard")
                userinput = input("Choose difficulty:")
            
                if userinput == "Easy":
                    printBoard(Easy)
                    



