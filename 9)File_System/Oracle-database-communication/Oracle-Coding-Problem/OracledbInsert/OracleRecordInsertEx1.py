#Program for Inserting the Records in Employee table
#OracleRecordInsertEx1.py
import oracledb as orc
def insertrecord():
    try:
        orc.init_oracle_client()
        con=orc.connect("system/manager@localhost/xe")
        cur=con.cursor()
        #Query for inserting the record
        iq="insert into employee values(300,'Travis', 22.22,'Numpy' )"
        cur.execute(iq)
        con.commit()
        print("Employee Record Inserted in Employee Table:")
    except orc.DatabaseError:
        print("Problem in Oracle DB")

#main program
insertrecord() # Function call
