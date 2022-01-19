#list the files and folders(listdirs())
#listfilesfolders.py
import os
try:
    names=os.listdir(r"C:\Users\mh36\Desktop\Azeem\Python-Function")
    for name in names:
        print("\t{}".format(name))
except FileNotFoundError:
     print("Folder does not exist to list files")