def InitializePuzzle():
    #A function that initializes the sudoku grid by reading a text file
    #The puzzle will have nine lines of nine numbers that are between 0 and 9 separated by commas
    #No inputs 
    #Outputs a sudoku grid

    grid = []
    text = open("SudokuPuzzle.txt", "r")
    puzzle = text.readlines()
    for line in range(len(puzzle)):
        if line != len(puzzle) - 1:
            puzzle[line] = puzzle[line][:-1]
            grid.append(list(map(int,puzzle[line].split(","))))
        else:
            grid.append(list(map(int,puzzle[line].split(","))))
    text.close()
    return grid

def PrintGrid(grid):
    #Prints the sudoku puzzle
    #Input - Grid that has 9 sublists with 9 numbers per sub list
    #Output - Prints out a typical sudoku board
    if not FindEmptySpaces(grid):
        print("Complete!")
    else:
        print("Incomplete!")

    for i in range(len(grid)):
        if i%3 == 0:
            print("-------------------")
            
        for j in range(len(grid[0])):
            if j%3 == 0:
                print("\b|", end ="")
            print(str(grid[i][j]) + " ", end = "")
        print("\b|")
    print("-------------------")
            

def FindEmptySpaces(grid):
    #Finds the next empty cell of the Sudoku grid by iterating from left to right and top to bottom
    #Input - Grid that has 9 sub lists with 9 numbers per sub list
    #Output - a tuple that represents the index of the empty cell

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i,j)
    return None

def IsValid(grid, num, pos):
    #Determines whether a number is valid or not in a specific location of the grid
    #Input - grid - 9 sub lists with 9 numbers per sub list
    #        num - any number that is 1-9
    #        pos - a tuple that represents an index of a cell
    #Output - True if the number is valid else false

    row = pos[0]
    col = pos[1]

    #check row
    for i in range(len(grid[0])):
        if grid[row][i] == num and col != i:
            return False
    
    #check column
    for i in range(len(grid)):
        if grid[i][col] == num and row != i:
            return False
        
    #check cell
    rowStart = row//3
    colStart = col//3
    for i in range(rowStart * 3, (rowStart * 3) + 3):
        for j in range(colStart * 3, (colStart * 3) + 3):
            if grid[i][j] == num and row != i and col != j:
                return False
            
    return True

def Solve(grid):
    #Uses the functions above to solve the sudoku puzzle
    #Input - Grid that is 9 sublists with 9 numbers per sublist
    #Output - returns true once the puzzle is solved else false

    emptySpace = FindEmptySpaces(grid)

    if not emptySpace:
        return True
    else:
        row, col = emptySpace

    for i in range(1,10):
        if IsValid(grid,i,emptySpace):
            grid[row][col] = i

            if Solve(grid):
                return True
            
            grid[row][col] = 0

    return False
     

grid = InitializePuzzle()
PrintGrid(grid)
Solve(grid)
PrintGrid(grid)



