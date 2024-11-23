#porogram for listing the File OR display the file names in folder
#ListFilesEx2.py
import os
try:
    foldername=input("Enter the Folder Name:")
    FileNames=os.listdir(foldername) # Here FileNames is an object of list type
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
