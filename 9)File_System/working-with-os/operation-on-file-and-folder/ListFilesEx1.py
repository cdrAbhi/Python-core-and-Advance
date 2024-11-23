#porogram for listing the File OR display the file names in folder
#ListFilesEx1.py
import os
try:
    FileNames=os.listdir("E:\\KVR-PYTHON-9AM\\FILES") # Here FileNames is an object of list type
    print("---------------------------------------------")
    print("List of Files")
    print("---------------------------------------------")
    for filename in FileNames:
        print("\t\t{}".format(filename))
    print("---------------------------------------------")
    print("Number of File={}".format(len(FileNames)))
    print("---------------------------------------------")
except FileNotFoundError:
    print("Folder does not exist")
