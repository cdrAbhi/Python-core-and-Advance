#program for Demonstarting getting the connection from Oracle DB
#OracleTestConEx2.py
import cx_Oracle # Step-1
con=cx_Oracle.connect("system/manager@127.0.0.1/XE") # Step-2
print("Python Program got Connection from Orale DB ")
print("Type of con=",type(con))
