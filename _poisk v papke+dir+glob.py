import pathlib
import shutil
import os

# define the path
currentDirectory = pathlib.Path(r'C:\Users\Admin\Desktop\Сетевая папка\ТО\PDF')

currentPattern = input('')

for to_pdf in currentDirectory.glob(currentPattern):
    print(to_pdf)

shutil.copy(to_pdf, r'C:\Users\Admin\Desktop\Сетевая папка\_ПЭС\На печать')

currentDirectory = pathlib.Path(r'C:\Users\Admin\Desktop\Сетевая папка\_ПЭС\На печать')

for currentFile in currentDirectory.glob(currentPattern):
    dirpath, filename = os.path.split(currentFile)
    shutil.move(currentFile, os.path.join(dirpath, r'Новая папка/' + filename))
    print(os.path.join(dirpath, r'Новая папка/' + filename))