# main.py
# Main program for Sudoku Solver
# Created by: 13518056 / Michael Hans

from sudoku import *
from reader import *

tesseractPath = 'C:/Users/micha/AppData/Local/Tesseract-OCR/tesseract.exe'
Grid = LoadFromText('tc2.txt')
print("Initialize Grid: ")
PrintGrid(Grid)
print("Sudoke Puzzle Solved!")
if (SolveTheGrid(Grid)):
    PrintGrid(Grid)