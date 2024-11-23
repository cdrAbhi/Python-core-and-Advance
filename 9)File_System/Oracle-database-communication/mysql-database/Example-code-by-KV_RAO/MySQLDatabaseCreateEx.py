#Program for creating a Database on the name of "9ambatch"
#MySQLDatabaseCreateEx.py
import mysql.connector
try:
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                passwd="root")
    cur=con.cursor()
    #design the Query and execute
    dc="create database 9ambatch"
    cur.execute(dc) # cur.execute("create database 9ambatch")
    print("Database Created in MySQL--verify")
except mysql.connector.DatabaseError as db:
    print("Problem in MySQL: ",db)