#rmdirex.py remove a folder
import os
try:
	os.rmdir("D:\KVR-HYD") # this is path where folder is ..
	print("Folder Removed--cerify")
except FileNotFoundError:
	print("Folder does not exists:")
except OSError:
	print("Folder Must be empty:")