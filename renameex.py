#renameex.py rename file name
import os
try: 
     os.rename("C:\AMPT","C:\KVR")
     print("Folder renamed cerified!!")
except FileNotFoundError:
     print("File name does not exist!!")
     