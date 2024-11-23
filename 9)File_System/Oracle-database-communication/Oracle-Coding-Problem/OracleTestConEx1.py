#program for Demonstarting getting the connection from Oracle DB
#OracleTestConEx1.py
import cx_Oracle # Step-1
try:
    con=cx_Oracle.connect("system1/manager@localhost/XE") # Step-2
    print("Python Program got Connection from Orale DB ")
    print("Type of con=",type(con))
except cx_Oracle.DatabaseError as db:
    print("Problem in Oracle: ", db)


