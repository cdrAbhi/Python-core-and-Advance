#program for Demonstarting getting the connection from Oracle DB
#OracleTestConEx3.py
import oracledb as orc
try:
    orc.init_oracle_client()
    con=orc.connect("system/manager@127.0.0.1/XE") # Step-2
    print("Python Program got Connection from Orale DB ")
    print("Type of con=",type(con))
except orc.DatabaseError as dbe:
    print("Problem at Database Software: ",dbe)