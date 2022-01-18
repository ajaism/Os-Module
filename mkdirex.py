#mkdirex.py creating folder
import os  #importing module
try:
     os.mkdir("Azeem")  # it creates new folder name as Azeem
     print("Folder create successfully!!")
except FileExistsError:
      print("Folder already exist!!")
