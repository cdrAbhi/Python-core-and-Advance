#program for deleting a Folder at a time
#RemoveFolder.py
import os
try:
    os.rmdir("c:\\INDIA")
    print("Folder Deleted --Verify")
except FileNotFoundError:
    print("Folder does not exist")
except OSError:
    print("Folder is not empty:")