#OracleDeleteEx1.py
import oracledb as orc
def deleterecord():
    try:
        orc.init_oracle_client()
        con = orc.connect("system/manager@localhost/orcl")
        cur = con.cursor()
        #Prepare the Query and execute
        dq="delete from employee where eno=300"
        cur.execute(dq)
        con.commit()
        print("{} Employee Record deleted".format(cur.rowcount))
    except orc.DatabaseError as db:
        print("Problem Oracle DB:",db)
#main program
deleterecord()