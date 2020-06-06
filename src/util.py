#print sudoku matrix in specific format
def printMatrix(matrix):
    content = "\n"
    for i in range(9): 
        for j in range(9): 
            content += " " + matrix[i][j]+ " "
            print(matrix[i][j], end = " ")
            if(j == 2 or j == 5):
                content += (" | ")
                print("|", end = " ")
        if(i == 2 or i == 5):
            content += ("\n----------|-----------|----------\n")
            print()
            print("------|-------|------")
        else:
            content += ("\n")
            print()
        
    return content