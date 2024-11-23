#Program for Demonstrating Cursor
#MySQLCursorTest.py
import mysql.connector
con=mysql.connector.connect(host="127.0.0.1",
                                            user="root",
                                            passwd="root")
print("Python Program Got Connection from MySQL Database")
print("--------------------------------------------------------------------")
cur=con.cursor()
print("Python Program created Cursor object")