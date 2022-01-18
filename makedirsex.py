#makedirsex.py  to create folder hierarchy 
import os
try: 
     os.makedirs("C:\India\Hyd\Ameerpet\Python") #on this path it will create folders hierarchy
     print("Folder hierarchy created...")
except FileExistsError:
     print("Folder Hierarchy already exists!!")
except FileNotFoundError:
     print("Drive name is Invalid!")