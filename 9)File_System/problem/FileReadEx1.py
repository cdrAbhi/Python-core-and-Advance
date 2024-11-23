#program for Reading the Data from File
#FileReadEx1.py
try:
    with open("E:\\KVR-PYTHON-9AM\\FILES\\NOTES\\hyd.info") as fp:
        filedata=fp.read()
        print("---------------------------------------")
        print(filedata)
        print("---------------------------------------")
except FileNotFoundError:
    print("File does not Exist:")
