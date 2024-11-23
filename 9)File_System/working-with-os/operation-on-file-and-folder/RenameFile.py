#Program for Renaming a File
#RenameFIle.py
import os
try:
    os.rename("hyd.py","main.py")
    print("File Name Renamed")
except FileNotFoundError:
    print("Source File Name does not Exist")
except FileExistsError:
    print("Destination File Name, we u are giving already exist")