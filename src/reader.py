# reader.py
# Extract sudoku grid from the image using Tesseract

from PIL import Image
import pytesseract
import cv2 as cv

# Load the grid from the unsolved sudoku image
def LoadFromImage(fileName, tesseractPath):
    pytesseract.pytesseract.tesseract_cmd = tesseractPath
    print(pytesseract.image_to_string(Image.open('../test/image1.png')))

# Load the grid from the txt file
def LoadFromText(fileName):
    f = open("../test/"+fileName, "r")
    text = f.read()
    f.close()
    grid = []
    rows = text.split("\n")
    for row in rows:
        converted_values = []
        raw_values = row.split(" ")
        for value in raw_values:
            if (value == '#'):
                converted_values.append(0)
            else:
                converted_values.append(int(value))
        grid.append(converted_values)
    return grid