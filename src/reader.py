# reader.py
# Extract sudoku grid from the image using Tesseract

from PIL import Image
import pytesseract
import re

# Load the grid from the image file
def LoadFromImage(fileName):
    # Setting up the tesseract-OCR
    tesseractPath = 'C:/Users/micha/AppData/Local/Tesseract-OCR/tesseract.exe'
    pytesseract.pytesseract.tesseract_cmd = tesseractPath
    img = Image.open("../test/"+fileName)
    width, height = img.size

    # Remove the thickness of the outer border
    img = img.crop((1, 1, width-1, height-1))
    width, height = img.size

    # Extract sudoku data / number from the image
    grid = []
    for i in range(9):
        row = []
        for j in range(9):
            # Crop every cell in the sudoku for better recognition by tesseract-OCR
            left = (width / 9) * j + 3
            top = (height / 9) * i + 3
            right = left + (width / 9) - 2
            bottom = top + (height / 9) - 2
            cropped = img.crop((left, top, right, bottom))
            value = pytesseract.image_to_string(cropped, lang='eng', config='--psm 6')

            # Remove all non-numeric character
            filtered = re.sub('[^0-9S]','', value)
            if (filtered == ''):
                row.append(0)
            elif (filtered == 'S'):
                row.append(5)
            else:
                row.append(int(filtered))
        grid.append(row)
    return grid

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