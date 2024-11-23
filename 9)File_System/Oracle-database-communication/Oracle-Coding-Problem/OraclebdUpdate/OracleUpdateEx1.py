#OracleUpdateEx1.py
import oracledb as orc
def recordupdate():
    try:
        orc.init_oracle_client()
        con=orc.connect("system/manager@localhost/orcl")
        cur=con.cursor()
        #design the query
        uq="update employee set sal=2.0,cname='TCS' where eno=500"
        cur.execute(uq)
        con.commit()
        print("{} Employee Reocrd Updated".format(cur.rowcount))
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)
#main program
recordupdate() # Functrion call