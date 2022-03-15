import os
 
dir_name = "C:\\Users\\LoyoL\\Desktop\\Python\\AutoCAD automation\\PDF"
test = os.listdir(dir_name)
 
for item in test:
    if item.endswith(".png"): # важно оставить точку (изменять после точки расширение файла)
        os.remove(os.path.join(dir_name, item))
