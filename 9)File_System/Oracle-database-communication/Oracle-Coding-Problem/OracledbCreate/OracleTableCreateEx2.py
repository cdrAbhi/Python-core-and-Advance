#program for cerating employee Table
#OracleTableCreateEx2.py
import oracledb as orc # Step-1
def tablecreate():
    try:
        orc.init_oracle_client()
        con=orc.connect("system/manager@localhost/xe") # Step-2
        cur=con.cursor() # Step-3
        #Step-4
        tq=input("Enter A Query for creating table in Oracle Database:")
        cur.execute(tq)
        #OR cur.execute(tq)
        print("Table  Created Sucessfully in Oracle DB")
    except orc.DatabaseError as db:
        print("Problem in Oracle Database: ", db)

#Main Program
tablecreate()

