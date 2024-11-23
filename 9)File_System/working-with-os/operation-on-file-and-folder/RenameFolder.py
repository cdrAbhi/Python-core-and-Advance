#Program for Renaming a Folder
#RenameFolder.py
import os
try:
    os.rename("C:\\Hindustan","C:\\india")
    print("Folder Renamed")
except FileNotFoundError:
    print("Source Folder Name does not Exist")
except FileExistsError:
    print("Destination Folder Name, we u are giving already exist")