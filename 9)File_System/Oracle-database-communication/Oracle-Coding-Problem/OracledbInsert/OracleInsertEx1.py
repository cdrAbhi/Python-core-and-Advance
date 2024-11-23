#OracleInsertEx1.py
import oracledb as orc
def recordinsert():
    while(True):
        try:
            orc.init_oracle_client()
            con=orc.connect("system/manager@localhost/orcl")
            cur=con.cursor()
            #accept the employee data from KBD
            print("-"*50)
            empno=int(input("Enter Employee Number:"))
            empname=input("Enter Employee Name:")
            empsal=float(input("Enter Employee Salary:"))
            compname=input("Enter Employee Comp Name:")
            print("-" * 50)
            #Prepare the query and execute
            iq="insert into employee values(%d,'%s',%f,'%s')"
            cur.execute(iq %(empno,empname,empsal,compname))
            #OR cur.execute("insert into employee values(%d,'%s',%f,'%s')" %(empno,empname,empsal,compname))
            con.commit()
            print("{} Employee Record Inserted".format(cur.rowcount))
            print("-" * 50)
            ch=input("Do u want to Insert Another Record(yes/no):")
            if(ch.lower()=="no"):
                print("Thx for using this Program:")
                break
        except orc.DatabaseError as db:
            print("Problem in Oracle DB:",db)
#main program
recordinsert()