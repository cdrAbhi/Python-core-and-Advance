#program for Displaying the content of any File
#FileReadEx3.py
try:
    filename=input("Enter Any File Name:")
    with open(filename,"r") as fp:
        filedata=fp.read()
        print("--------------------------------------------------")
        print("Content of '{}' File:".format(filename))
        print("--------------------------------------------------")
        print("{}".format(filedata))
        print("--------------------------------------------------")
except FileNotFoundError:
    print("File Does not Exist")


