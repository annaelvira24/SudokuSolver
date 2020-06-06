
# loads text file into sudoku matrix
def loadTextFile(file):
    f = open(file)
    text = f.read()
    lines = text.split('\n')
    f.close()

    matrix = [[-1 for i in range(9)] for j in range(9)]

    for i in range(9) :
        grids = lines[i].split(" ")
        for j in range (9) :
            matrix[i][j] = grids[j]
    
    return matrix


    