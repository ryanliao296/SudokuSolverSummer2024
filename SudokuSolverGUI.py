from tkinter import *

root = Tk()
root.title("Sudoku Solver")
root.geometry("325x550")

label = Label(root, text = "Fill in the numbers and click Solve!").grid(row = 0, column = 1, columnspan = 10)

errLabel = Label(root, text = "", fg = "red")
errLabel.grid(row = 15, column = 1, columnspan = 10, pady = 5)

solvedLabel = Label(root, text = "", fg = "green")
solvedLabel.grid(row = 15, column = 1, columnspan = 10, pady = 5)

cells = {}

def ValidateNumber(x):
    out = (x.isdigit() or x == "") and len(x) < 2
    return out

reg = root.register(ValidateNumber)

def Grid3x3(row, column, bgcolor):
    for i in range(3):
        for j in range(3):
            e = Entry(root, width = 5, bg = bgcolor, justify = "center", validate = "key", validatecommand = (reg, "%P"))
            e.grid(row = row + i + 1, column = column + j + 1, sticky = "nsew", padx = 1, pady = 1, ipady = 5)
            cells[(row + i + 1, column + j + 1)] = e

def Grid9x9():
    color = "#D0ffff"
    for rowNum in range(1,10,3):
        for colNum in range(0,9,3):
            Grid3x3(rowNum, colNum, color)
            if color == "#D0ffff":
                color = "#ffffd0"
            else:
                color = "#D0ffff"

def ClearValues():
    errLabel.configure(text = "")
    solvedLabel.configure(text = "")
    for row in range(2,11):
        for col in range(1,10):
            cell = cells[(row,col)]
            cell.delete(0, "end")

def GetValues():
    grid = []
    errLabel.configure(text = "")
    solvedLabel.configure(text = "")
    for row in range(2,11):
        rows = []
        for col in range(1,10):
            val = cells[(row,col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))
        grid.append(rows)

btn = Button(root, command = GetValues, text = "Solve!", width = 10)
btn.grid(row = 20, column = 1, columnspan = 5, pady = 20)

btn = Button(root, command = ClearValues, text = "Reset", width = 10)
btn.grid(row = 20, column = 5, columnspan = 5, pady = 20)

Grid9x9()
root.mainloop()