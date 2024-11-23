#Program for Reading student data from KBD and save them in file
#FileWriteEx5.py
#Read the Data from KBD
with open("student.data","at") as fp:
    while(True):
        sno=input("Enter Student Number:")
        sname=input("Enter Student Name:")
        marks=input("Enter Student Marks:")
        #write the student to the file
        fp.write(sno+"\t")
        fp.write(sname+"\t")
        fp.write(marks+"\n")
        print("Student Data Saved into the file")
        print("-------------------------------------------")
        ch=input("Do u want to insert one record(yes/no):")
        if(ch.lower()=="no"):
            print("thx for using this program")
            break



