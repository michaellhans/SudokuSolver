# main.py
# Main program for Sudoku Solver
# Created by: 13518056 / Michael Hans

from sudoku import *
from reader import *
import time
import sys

tesseractPath = 'C:/Users/micha/AppData/Local/Tesseract-OCR/tesseract.exe'

print("Sthyrelest Enterprise - Sudoku Solver")
print("Created by: 13518056 / Michael Hans")

print()
print("Section 1: Load Sudoku Grid")
print("Terdapat dua metode pengambilan grid: ")
print("1. Load from Image")
print("2. Load from Text File")
print("Pilih salah satu metode dari dua metode di atas: ",end='')
choice = int(input())

if (choice == 1):
    print("Masukkan nama file gambar yang ingin diambil: ",end='')
    fileName = input()
    print("Please wait for extracting ...")
    Grid = LoadFromImage(fileName)
    fileName = fileName + '-result.txt'
    print("Pengambilan grid sudoku dari file gambar berhasil!")
else:
    print("Masukkan nama file text yang ingin diambil: ",end='')
    fileName = input()
    Grid = LoadFromText(fileName)
    print("Pengambilan grid sudoku dari file text berhasil!")
    fileName = fileName + '-result.txt'

print()
print("Section 2: Grid Sudoku Awal")
print("Kondisi awal Grid Sudoku: ")
PrintGrid(Grid)

print()
input("Tekan ENTER untuk melanjutkan program ...")
print()
print("Section 3: Solving the Grid")
print("Please wait ...")
time_origin = time.time()

if (SolveTheGrid(Grid)):
    print()
    print("Sudoke Puzzle Solved!")
    PrintGrid(Grid)
    print()

    # Menuliskan semua koordinat dengan area bernomor 5
    listOfCoordinate = GetAllCoordinate(Grid, 5)
    PrintCoordinate(listOfCoordinate, 5)
    time_end = time.time()
    
    print()
    print("Waktu yang diperlukan untuk menyelesaikan Grid Sudoku adalah "+str(time_end - time_origin)+" detik")

    # Menuliskan output ke text file
    original_stdout = sys.stdout # Save a reference to the original standard output

    with open("../result/"+fileName,"w+") as f:
        sys.stdout = f # Change the standard output to the file we created.
        PrintGrid(Grid)
        print()
        PrintCoordinate(listOfCoordinate, 5)
        sys.stdout = original_stdout # Reset the standard output to its original value

    print("Hasil sudoku berhasil disimpan!")
    print("Hasil sudoku disimpan pada ./result/"+fileName)

else:
    print("Maaf, grid sudoku tidak dapat diselesaikan!")

print()
input("Click ENTER to end the program ...")