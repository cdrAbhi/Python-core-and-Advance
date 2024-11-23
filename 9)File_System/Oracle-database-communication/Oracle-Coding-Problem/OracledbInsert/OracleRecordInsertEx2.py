#Program for Inserting the Records in Employee table
#OracleRecordInsertEx2.py
import oracledb as orc
def insertrecord():
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
    except orc.DatabaseError as db:
        print("Problem in Oracle DB: ",db)

#main program
insertrecord() # Function call
