#OracleUpdateEx3.py
import oracledb as orc
def recordupdate():
    while(True):
        try:
            orc.init_oracle_client()
            con=orc.connect("system/manager@localhost/orcl")
            cur=con.cursor()
            #design the query
            empno=int(input("Enter Employee Number for updating other details:"))
            empsal=float(input("Enter Employee New Salary:"))
            compname=input("Enter Employee New Comp Name:")
            uq="update employee set sal=%f,cname='%s' where eno=%d"
            cur.execute(uq %(empsal,compname,empno))
            #OR cur.execute("update employee set sal=%f,cname='%s' where eno=%d" %(empsal,compname,empno))
            con.commit()
            if(cur.rowcount>0):
                print("{} Employee Record Updated".format(cur.rowcount))
            else:
                print("Employee Record does not Exist")
            print("-"*50)
            ch=input("Do u want to update Another Record(yes/no):")
            if(ch.lower()=="no"):
                print("Thx for using this program")
                break
        except orc.DatabaseError as db:
            print("Problem in Oracle DB:",db)
#main program
recordupdate() # Functrion call