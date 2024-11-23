# write a python program which will create a database .
try:
    import mysql.connector 
    
    con=mysql.connector(host="localhost",
                        user="database-username",
                        passwd="mysql-passwd")
    cur=con.cursor()
    que="create database 9:00AM"
    cur.execute(que)
    print("database create in mysql succesfully")
except mysql.connector.DatabaseError as dbErr:
    print(f"problem in database : {}")