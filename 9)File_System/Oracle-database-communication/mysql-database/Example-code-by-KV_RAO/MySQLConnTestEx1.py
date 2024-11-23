#Program for demonstrating Connection from MySQL Database
#MySQLConnTestEx1.py
import mysql.connector
con=mysql.connector.connect(host="localhost",
                                            user="root",
                                            passwd="root")
print("Python Program Got Connection from MySQL Database")