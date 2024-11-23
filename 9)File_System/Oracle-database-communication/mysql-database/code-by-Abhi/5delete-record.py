# write a python program which will delete the records by except base on employee number

import mysql.connector as db

def delTable():
    while True:
        try:
            con=mysql.connector.connect(host="localhost",
                                        user="username",
                                        passwd="mysql-passwd",
                                        database="9:00AM")
            cur=con.cursor()
           # query and execut
            query="delete from employee where Name=Ravi Das"
            cur.execute(query)
            con.commit()
            if cur.rowount>0:
                print("Record deleted succesfully")
            else:
                print("Record doesn't exit in empoyee table")
            o=input("Enter Do you want to delete another record(yes/no) : ")
            if o.lower()=='no':
                break
        except db.DatabaseError as dbErr:
            print(f"Error occur in Database : {dbErr}")
    
