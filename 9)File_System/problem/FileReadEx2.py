#program for Reading the Data from File
#FileReadEx2.py
try:
    with open("stud.data") as fp:
        filedata=fp.readlines()
        print("---------------------------------------")
        for record in filedata:
            print(record,end="")
        print("---------------------------------------")
except FileNotFoundError:
    print("File does not Exist:")
