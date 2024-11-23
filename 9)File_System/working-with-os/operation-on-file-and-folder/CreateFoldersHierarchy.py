#Program for creating Folder Hierarchy---
#CreateFoldersHierarchy.py---makedirs()
import os
try:
    os.makedirs("C:\\INDIA\\HYD")
    print("Folder Hierarchy Created --Verfy")
except FileExistsError:
    print("Folders Hierarchy already Created ")