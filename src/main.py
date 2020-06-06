from loadFile import *
from sudokuSolver import *
from extractImage import *
from util import *

def printAndSolve(matrix, file):
    file2write=open("../result/"+ file[8:] +"-result.txt",'w')
    content = " "
    print("Initial sudoku:")
    printMatrix(matrix)
    solve(matrix)
    print("\nSolved sudoku:")
    content += printMatrix(matrix)
    content += "\nFive positions are:"
    print("\nFive positions are:")
    fives = findFive(matrix)
    content += (printFiveCoord(fives))

    file2write.write(content)
    file2write.close()


print("==================== WELCOME TO SUDOKU SOLVER ====================")
choice = 0
while (not choice == 3):
    print("\nMenu:")
    print("1. Input Text File\n2. Input Image File\n3. Exit")
    choice = int(input())

    if(choice == 1):
        print("Please enter testcase file path here in .txt format", end = " ")
        text = str(input())
        matrix = loadTextFile(text)
        printAndSolve(matrix, text)
    elif(choice == 2):
        print("Please enter testcase file path here in .png format", end = " ")
        img = str(input())
        matrix = extractImage(img)
        printAndSolve(matrix, img)
    elif(choice == 3):
        print("Good Bye")
    else:
        print("Invalid input!")

