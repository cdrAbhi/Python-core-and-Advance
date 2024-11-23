#Program for displaying Records along with Column Names of any table
#MySQLSelectWithColNames.py
import mysql.connector
def  selectrecords():
    try:
        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="root",
                                      database="9ambatch")
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

    except mysql.connector.DatabaseError as db:
        print("Problem in MySQL  DB:",db)
#main program
selectrecords()