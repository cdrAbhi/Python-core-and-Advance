#Program Reading the Records from table by using fetchone()
#OracleSelectEx1.py
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
        while(True):
            record = cur.fetchone()
            if(record!=None):
                for val in record:
                    print("{}".format(val),end="\t\t")
                print()
            else:
                print("*" * 50)
                break

    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)
#main program
selectrecords()