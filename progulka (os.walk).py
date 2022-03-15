import os

for root, dirs, files in os.walk(r"C:\Users\LoyoL\Desktop\Python\AutoCAD automation"):
    for filename in files:
        print(filename)