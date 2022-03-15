import os, fnmatch, shutil

listOfFiles = os.listdir(r'C:\Users\LoyoL\Desktop\Python\AutoCAD automation')
pattern = input('') # что искать (работает со *) пример (*.py) - файлы с расширением .py
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
            print(entry)