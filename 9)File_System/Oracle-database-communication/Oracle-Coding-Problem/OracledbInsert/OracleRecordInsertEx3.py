#Program for Inserting the Records in Employee table
#OracleRecordInsertEx3.py
import oracledb as orc
def insertrecord():
    while(True):
        try:
            orc.init_oracle_client()
            con=orc.connect("system/manager@localhost/xe")
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
        except orc.DatabaseError as db:
            print("Problem in Oracle DB: ",db)

#main program
insertrecord() # Function call
