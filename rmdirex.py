#rmdirex.py remove a folder
import os
try:
	os.rmdir("D:\KVR-HYD")
	print("Folder Removed--cerify")
except FileNotFoundError:
	print("Folder does not exists:")
except OSError:
	print("Folder Must be empty:")