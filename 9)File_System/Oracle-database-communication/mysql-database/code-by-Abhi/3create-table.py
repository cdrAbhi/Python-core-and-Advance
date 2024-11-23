# write a python program which will create a table employee with suitable colums in 9:00Am database of mysql

import mysql.connector

def tablecreate():
    try:
        con=mysql.connector(host"localhost",
                            user="mysql-name",
                            passwd="mysql-password",
                            database="9:00AM")
        cur=con.cursor()
        tq="create table empoyee(eno int primary key,name varchar(10) not null,sal real,cname varchar(10) not null)"
        cur.execute(tc)
        print("Table create Succesfully in MySQL")
    except mysql.connector.DatabaseError as db:
        prit(f"problem in database : {}")
                            
                            
                            
                            