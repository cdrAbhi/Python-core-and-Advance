#program for cerating employee Table
#OracleTableCreateEx1.py
import oracledb as orc # Step-1
def tablecreate():
    try:
        orc.init_oracle_client()
        con=orc.connect("system/manager@localhost/xe") # Step-2
        cur=con.cursor() # Step-3
        #Step-4
        tq="create table employee (eno number(2) primary key, name varchar2(10) not null, sal number(5,2) not null)"
        cur.execute(tq)
        #OR cur.execute("create table employee (eno number(2) primary key, name varchar2(10) not null, sal number(5,2) not null)")
        print("Table  Created Sucessfully in Oracle DB")
    except orc.DatabaseError as db:
        print("Problem in Oracle Database: ", db)

#Main Program
tablecreate()

