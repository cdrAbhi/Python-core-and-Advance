#Program for Removing the Table Name from Oracle Database
#OracleDropTable.py
import oracledb as orc
def tabledrop():
    try:
        orc.init_oracle_client()
        con=orc.connect("system/manager@127.0.0.1/xe")
        cur=con.cursor()
        #step-4
        cur.execute("drop table book")
        print("Table Droped --verify")
    except orc.DatabaseError as db:
        print("Problem in Oracle DB: ",db)
 #main program
tabledrop() # Function Call
