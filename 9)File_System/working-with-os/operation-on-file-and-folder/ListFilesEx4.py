#porogram for listing only Python Files
#ListFilesEx3.py
import os
try:
    foldername=input("Enter the Folder Name:")
    FileNames=os.listdir(foldername) # Here FileNames is an object of list type
    print("---------------------------------------------")
    print("List of Files")
    print("---------------------------------------------")
    nopy=0
    for filename in FileNames:
        if(filename.endswith(".py")):
            nopy=nopy+1
            print("\t\t{}".format(filename))
    print("---------------------------------------------")
    print("Number of Files={}".format(len(FileNames)))
    print("Number of Python Files={}".format(nopy))
    print("---------------------------------------------")
except FileNotFoundError:
    print("Folder does not exist")
