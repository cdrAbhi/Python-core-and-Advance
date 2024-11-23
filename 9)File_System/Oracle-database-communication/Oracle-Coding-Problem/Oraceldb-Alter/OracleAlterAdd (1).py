#Program adding the columns  to the Table in Oracle DB
#OracleAlterAdd.py
import oracledb as orc
def alterwithadd():
    try:
        orc.init_oracle_client()
        con=orc.connect("system/manager@127.0.0.1/xe")
        cur=con.cursor()
        #step-4
        aq="alter table employee add(cname varchar2(10) not null)"
        cur.execute(aq)
        print("Table altered --verify")
    except orc.DatabaseError as db:
        print("Problem in Oracle DB: ",db)
#main program
alterwithadd() # Function Call