#OracleDeleteEx2.py
import oracledb as orc
def deleterecord():
    while(True):
        try:
            orc.init_oracle_client()
            con = orc.connect("system/manager@localhost/orcl")
            cur = con.cursor()
            #Prepare the Query and execute
            print("-" * 40)
            empno=int(input("Enter Employee Number:"))
            #dq="delete from employee where eno=%d"
            cur.execute("delete from employee where eno=%d" %empno)
            con.commit()
            if(cur.rowcount>0):
                print("{} Employee Record Deleted".format(cur.rowcount))
            else:
                print("Employee Record Does not Exist")
            print("-"*40)
            ch = input("Do u want to Delete Another Record(yes/no):")
            if (ch.lower() == "no"):
                print("Thx for using this Program:")
                break
        except orc.DatabaseError as db:
            print("Problem Oracle DB:",db)
#main program
deleterecord()