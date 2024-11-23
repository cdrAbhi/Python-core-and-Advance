#Program for displaying Records along with Column Names of any table
#OracleDisplayTableData.py
import oracledb as orc
def  selectrecords():
    try:
        orc.init_oracle_client()
        con=orc.connect("system/manager@localhost/xe")
        cur=con.cursor()
        #accept the table name
        tname=input("Enter Table Name:")
        sq="select * from %s " %tname
        cur.execute(sq)
        #Code of  getting column names
        print("*" * 50)
        #here description is a pre-defined attribute present in cursor object and gives Columns Information of a table
        colinfo=cur.description
        for col in colinfo:
            print(col[0],end="\t\t")
        print()
        print("*"*50)
        #Code for Getting Records
        records = cur.fetchall()
        for record in records:
            for val in record:
                print("{}".format(val), end="\t\t")
            print()
        print("*" * 50)

    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)
#main program
selectrecords()