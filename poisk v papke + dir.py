import pathlib

# define the path
currentDirectory = pathlib.Path(r'C:\Users\LoyoL\Desktop\Python\Del files\1')

for currentFile in currentDirectory.iterdir():
    print(currentFile)