#Program for Inserting the Records in Employee table
#MySQLRecordInsertEx.py
import mysql.connector
def insertrecord():
    while(True):
        try:
            con = mysql.connector.connect(host="localhost",
                                          user="root",
                                          passwd="root",
                                          database="9ambatch")
            cur=con.cursor()
            #Query for inserting the record
            #accept employee details from KBD
            print("-------------------------------------------------------")
            empno=int(input("Enter Employee Number:"))
            empname=input("Enter Employee Name:")
            empsal=float(input("Enter Employee Salary:"))
            empcmpname=input("Enter Employee  Comp Name:")
            print("-------------------------------------------------------")
            iq="insert into employee values(%d,'%s' ,%f,'%s' )"
            cur.execute(iq %(empno,empname,empsal,empcmpname))
            #OR cur.execute("insert into employee values(%d,'%s' ,%f,'%s' )" %(empno,empname,empsal,empcmpname))
            con.commit()
            print("{} Employee Record Inserted in Employee Table:".format(cur.rowcount))
            print("-------------------------------------------------------")
            ch=input("Do u want to Insert Another Record(yes/no): ")
            if(ch.lower()=="no"):
                print("Thx for using program")
                break
        except mysql.connector.DatabaseError as db:
            print("Problem in MySQL DB: ",db)

#main program
insertrecord() # Function call
