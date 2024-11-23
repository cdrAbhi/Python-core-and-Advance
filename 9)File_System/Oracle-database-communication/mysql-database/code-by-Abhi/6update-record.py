# write a python program which will update salary and company name of employee table of mysqldatabase

from mysql.connector as db 
def updTable():
    while True:
        try:
            con=mysql.connector.connect(host="localhost",
                                        user="username",
                                        passwd="mysql-passwd",
                                        database="9:00AM")
            cur=con.cursor()
            sl=input("Employee salary : ")
            compName=input("Employee Company Name : ")
            EmpNum=input("Employee Number : ")
            que="update employee set sal=%f,compname='%s' where eno=%d"
            cur.execute(que%(sl,compName,EmpNum))
            con.commit()
            if cur.rowount>0:
                    print("Employee Record Updated succesfully")
            else:
                print("Employee Record doesn't exit in empoyee table")
            o=input("Enter Do you want to update another record(yes/no) : ")
            if o.lower()=='no':
                break           
        except db.DatabaseError as dbErr:
            print(f"Error in database : {dbErr}")