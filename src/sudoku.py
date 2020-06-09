# sudoku.py
# Contain all procedure and function about sudoku

# Print the grid to the output screen
def PrintGrid(Grid):
    for i in range(9):
        if ((i+1) % 3 == 1):
            print('+-------+-------+-------+')
        print('|',end=' ')
        for j in range(9):
            if (Grid[i][j] == 0):
                printedValue = '.'
            else:
                printedValue = Grid[i][j]
            if ((j+1) % 3 == 0):
                print(printedValue,end=' | ')
            else:
                print(printedValue,end=' ')
        print()
    print('+-------+-------+-------+')

# Fill the sudoku grid
def FillTheGrid(Grid, i, j):
    if (i < 9):
        # If the cell[i][j] has already assigned
        if (Grid[i][j] > 0):
            if (j+1 == 9):
                return (FillTheGrid(Grid, i+1, 0))
            else:
                return (FillTheGrid(Grid, i, j+1))
        
        # If the cell[i][j] is empty
        else:
            PossibleSolution = []
            for value in range(1, 10):
                if (CheckAvailability(Grid, i, j, value)):
                    PossibleSolution.append(value)

            # If there is no candidate solution, return False
            if (len(PossibleSolution) == 0):
                return False
            else:
                for value in PossibleSolution:
                    Grid[i][j] = value
                    if (j+1 == 9):
                        if (FillTheGrid(Grid, i+1, 0)):
                            return True
                        else:
                            Grid[i][j] = 0
                    else:
                        if (FillTheGrid(Grid, i, j+1)):
                            return True
                        else:
                            Grid[i][j] = 0
                return False
    # If the index out of bound, stop the searching
    # It means every cell in the grid has been filled
    else:
        return True

# Solver for Sudoku
def SolveTheGrid(Grid):
    if IsGridFull(Grid):
        print("The grid has already finished!")
        return True
    else:
        return FillTheGrid(Grid, 0, 0)
        
# Boolean Checker
# Check if the value has already assigned in row
def CheckInRow(Grid, row, value):
    found = False
    for i in range(9):
        if (Grid[row][i] == value):
            found = True
            break
    return found

# Check if the value has already assigned in column
def CheckInColumn(Grid, column, value):
    found = False
    for i in range(9):
        if (Grid[i][column] == value):
            found = True
            break
    return found

# Check if the value has already assigned in subgrid
def CheckInSubGrid(Grid, row, column, value):
    found = False
    for i in range(3):
        for j in range(3):
            rowPos = int(row/3) * 3 + i
            columnPos = int(column/3) * 3 + j
            if (Grid[rowPos][columnPos] == value):
                found = True
    return found

# Sudoku rules: check availability value in certain row, column, and subgrid
def CheckAvailability(Grid, row, column, value):
    return not(CheckInRow(Grid, row, value) or CheckInColumn(Grid, column, value) or CheckInSubGrid(Grid, row, column, value))

# Check if the grid is already full of numbers
def IsGridFull(Grid):
    for i in range(9):
        for j in range(9):
            if (Grid[i][j] == 0):
                return False
    return True