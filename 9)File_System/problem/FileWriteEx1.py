#program for writing the Data to the file
#FileWriteEx1.py
with open("stud.data","a") as fp:
    fp.write(str(30)+"\t")
    fp.write("DR"+"\t")
    fp.write(str(42.12)+"\n")
    print("Data written to the file")