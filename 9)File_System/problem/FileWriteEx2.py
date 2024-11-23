#program for writing the Data to the file
#FileWriteEx2.py
x= {10:"Python",20:"Java",30:"HTML"}
with open("stud1.data","a") as fp:
    fp.writelines(str(x)+"\n")
    print("Data written to the File")

