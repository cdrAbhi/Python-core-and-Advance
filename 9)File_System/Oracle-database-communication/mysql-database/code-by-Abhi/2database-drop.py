# program for droping or removing database

# write a python program which will drop or remove any data basestring
try:
    import mysql.connector
    con=mysql.connector(host="localhost",
                        user="mysql-username",
                        passwd="mysql_password")
                        
    cur=con.cursor()
    que="drop database stuedent"
    cur.execute(que)
    print("database student remove successfully")
except mysql.connectot.DatabaseError as db:
   print(f"problem in database : {}") 