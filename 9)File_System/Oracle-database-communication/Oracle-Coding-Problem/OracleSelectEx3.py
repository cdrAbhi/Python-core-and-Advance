#Program Reading the Records from table by using fetchall()
#OracleSelectEx3.py
import oracledb as orc
def  selectrecords():
    try:
        orc.init_oracle_client()
        con=orc.connect("system/manager@localhost/xe")
        cur=con.cursor()
        #DRL Query
        sq="select * from employee"
        cur.execute(sq)
        print("*"*50)
        records = cur.fetchall()
        for record in records:
            for val in record:
                print("{}".format(val),end="\t\t")
            print()
        print("*" * 50)
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)
#main program
selectrecords()