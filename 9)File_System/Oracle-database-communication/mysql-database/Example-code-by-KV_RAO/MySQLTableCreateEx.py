#Program for creating a Table employee in 9ambatch of MYSQL
#MySQLTableCreateEx.py
import mysql.connector
def  tablecreate():
    try:
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="root",
                                    database="9ambatch")
        cur=con.cursor()
        #Design the Query and execute
        tc="create table student(sno int primary key,name varchar(10) not null,marks float not null, cname varchar(10) not null)"
        cur.execute(tc)
        print("Table Created Sucessfully in MySQL")
    except mysql.connector.DatabaseError as db:
        print("Problem in MySQL: ", db)

#main program
tablecreate()