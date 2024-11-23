#Program for Dropinng OR removig the Database from MYSQL
#MySQLDatabaseDropEx.py
import mysql.connector
def  dropdatabase():
    try:
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="root")
        cur=con.cursor()
        #design the Query and execute
        cur.execute("drop database student")
        print("Database Removed from  MySQL--verify")
    except mysql.connector.DatabaseError as db:
        print("Problem in MySQL: ",db)
#main program
dropdatabase() # Function call