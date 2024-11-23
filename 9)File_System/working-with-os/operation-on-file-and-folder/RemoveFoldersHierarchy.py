#Program for Removing  Folders Hierarchy
#RemoveFoldersHierarchy.py
import os
try:
    os.removedirs("C:\\KVR\\PYTHON")
    print("Folder(s) Hierachy deleted")
except FileNotFoundError:
    print("Folder(s) Hierachy Does not Exist")
except OSError:
    print("Folder(s) Hierachy  is not Empty")