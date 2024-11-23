#Program for Reading student data from KBD and save them in file
#FileWriteEx4.py
#Read the Data from KBD
sno=input("Enter Student Number:")
sname=input("Enter Student Name:")
marks=input("Enter Student Marks:")
#write the student to the file
with open("student.data","at") as fp:
    fp.write(sno+"\t")
    fp.write(sname+"\t")
    fp.write(marks+"\n")
    print("Student Data Saved into the file")
    print("-------------------------------------------")

