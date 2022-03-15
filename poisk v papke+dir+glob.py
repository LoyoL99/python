import pathlib

# define the path
currentDirectory = pathlib.Path(r'C:\Users\LoyoL\Desktop\Python\AutoCAD automation')

currentPattern = "*.png"

for currentFile in currentDirectory.glob(currentPattern):
    print(currentFile)