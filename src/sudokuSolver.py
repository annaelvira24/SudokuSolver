# find the empty cell of a sudoku matrix
def findEmptyCell(matrix):
    emptyCell = [-1, -1]
    for i in range (9):
        for j in range (9):
            if(matrix[i][j] == '#'):
                emptyCell[0] = i
                emptyCell[1] = j       
                return emptyCell
            
    return emptyCell

# check if num is already exist in the row 
def checkRow(matrix, row, num):
    for i in range (9):
        if(matrix[row][i] == num):
            return True
    
    return False

# check if num is already exist in the col
def checkColumn(matrix, col, num):
    for i in range (9):
        if(matrix[i][col] == num):
            return True
    
    return False

# check if num is already exist in the 3x3 square
def checkSquare(matrix, row, col, num):
    row -= row%3
    col -= col%3

    for i in range(3):
        for j in range(3):
            if(matrix[row+i][col+j] == num):
                return True
    
    return False

# check wether it is safe to place num in a specific cell
def isSafe(matrix, row, col, num):
    return (not checkColumn(matrix, col, num) and not checkRow(matrix, row, num) and not checkSquare(matrix, row, col, num))

#solve sudoku
def solve(matrix):
    emptyCell = findEmptyCell(matrix)
    # Basis, if there's no empty cell left. We have finished!
    if(emptyCell[0] == -1):
        return True

    row = emptyCell[0]
    col = emptyCell[1]
    
    # iterate from 1 to 9
    for num in range (1,10):
        # check the cell is safe or not to put num
        if(isSafe(matrix, row, col, str(num))):
            matrix[row][col] = str(num)

            #recursively test the solution
            if(solve(matrix)):
                return True
            
            # num is not in correct cell
            else:
                matrix[row][col] = '#'
    
    # Triggers backtracking
    return False

# Function to find 5 cells' coordinate
def findFive(matrix):
    result = []
    for i in range (9):
        for j in range(9):
            if(matrix[i][j] == '5'):
                result.append([i, j])

    return result

def printFiveCoord(result):
    content = "\n"
    for item in result :
        content += "(" + str(item[0])+ "," + str(item[1]) + ")\n"
        print("(" + str(item[0])+ "," + str(item[1]) + ")")
    
    return content
    

