# write a python program which will alter the column sizes
# write a python program which will remove the table 
# write a pthon program which will insert records in empoyee table

# write a python program which will inseret a record in employee table by accepting employee value from keyboard.
#================================================================================ 
#NOw we can use insertExm as a module to other file
import mysql.connector,sys
def insTable():
    while True:
        try:
            con=mysql.connector.connect(host="localhost",
                                        user="username",
                                        passwd="mysql-passwd",
                                        database="9:00AM")
            cur=con.cursor()
            # design the query and export it
            empnum=input("Enter employee number : ")
            empname=input("Enter employee name : ")
            empsal=input("Enter employee sal : ")
            empCn=input("Enter employee company name : ")
            
            qry="insert into employee values (%d,%s,%d,%s)"
            cur.execute(qry%(empnum,empname,empsal,empCn))
            con.commit()
            
            print(f"Employee recod insert in Emloyee table at row{cur.rowcount}")
            print("#"*50)
            o=input("Do you want to insert another record(yes/no) : ")
            if o.lower()=="no":
                sys.exit()
        except mysql.connector.DatabaseError as db:
            print(f"problem in database : {db}")
