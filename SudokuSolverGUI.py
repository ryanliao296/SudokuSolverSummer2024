from tkinter import *
from SudokuSolver import InitializePuzzle, PrintGrid, FindEmptySpaces, IsValid, Solve
#Import functions to solve puzzle from SudokuSolver.py

#Create the GUI window
root = Tk()
root.title("Sudoku Solver")
root.geometry("325x550")

#Create a label for the top of the window
label = Label(root, text = "Fill in the numbers and click Solve!").grid(row = 0, column = 1, columnspan = 10)

#Labels for Completion and error messages
errLabel = Label(root, text = "", fg = "red")
errLabel.grid(row = 15, column = 1, columnspan = 10, pady = 5)

solvedLabel = Label(root, text = "", fg = "green")
solvedLabel.grid(row = 15, column = 1, columnspan = 10, pady = 5)

#Dictionary that stores the entries for each cell
cells = {}


def ValidateNumber(x):
    #Function that validates an input is a single digit or empty
    out = (x.isdigit() or x == "") and len(x) < 2
    return out

#Register the validation function with Tkinter
reg = root.register(ValidateNumber)

def Grid3x3(row, column, bgcolor):
    #Creates a 3x3 grid of entry widgets
    for i in range(3):
        for j in range(3):
            e = Entry(root, width = 5, bg = bgcolor, justify = "center", validate = "key", validatecommand = (reg, "%P"))
            e.grid(row = row + i + 1, column = column + j + 1, sticky = "nsew", padx = 1, pady = 1, ipady = 5)
            cells[(row + i + 1, column + j + 1)] = e

def Grid9x9():
    #Creates the entire 9x9 Sudoku grid
    color = "#D0ffff"
    for rowNum in range(1,10,3):
        for colNum in range(0,9,3):
            Grid3x3(rowNum, colNum, color)
            if color == "#D0ffff":
                color = "#ffffd0"
            else:
                color = "#D0ffff"

def ClearValues():
    #clears all values from the grid
    errLabel.configure(text = "")
    solvedLabel.configure(text = "")
    for row in range(2,11):
        for col in range(1,10):
            cell = cells[(row,col)]
            cell.delete(0, "end")

def IsInitialGridValid(grid):
    #Ensures the initial input is valid and solvable
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                num = grid[i][j]
                grid[i][j] = 0
                if not IsValid(grid, num, (i, j)):
                    grid[i][j] = num
                    return False
                grid[i][j] = num
    return True


def GetValues():
    #Gets the values from the grid and updates the grid
    grid = []
    errLabel.configure(text = "")
    solvedLabel.configure(text = "")
    try:
        for row in range(2,11):
            rows = []
            for col in range(1,10):
                val = cells[(row,col)].get()
                if val == "":
                    rows.append(0)
                else:
                    rows.append(int(val))
            grid.append(rows)
        
        #check the initial grid is valid configuration and solvable
        if not IsInitialGridValid(grid):
            errLabel.configure(text = "Invalid Sudoku puzzle")
            return
        
        if Solve(grid):
            UpdateGrid(grid)
            solvedLabel.configure(text = "Puzzle Solved!")
        else:
            errLabel.configure(text = "No solution exists")
    except ValueError:
        errLabel.configure(text = "Invalid input, enter numbers between 1-9")

def UpdateGrid(grid):
    #updates the grid with solved values
    for row in range(2,11):
        for col in range(1,10):
            val = grid[row - 2][col - 1]
            cells[(row,col)].delete(0,"end")
            if val != 0:
                cells[(row,col)].insert(0, str(val))

#Buttons that solve and reset hte grid
btn = Button(root, command = GetValues, text = "Solve!", width = 10)
btn.grid(row = 20, column = 1, columnspan = 5, pady = 20)

btn = Button(root, command = ClearValues, text = "Reset", width = 10)
btn.grid(row = 20, column = 5, columnspan = 5, pady = 20)

#create the 9x9 grid and loop
Grid9x9()
root.mainloop()