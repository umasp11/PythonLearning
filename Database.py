'''
MySQL is a DBMS which is used to manage the database like store and retrieve the data
to make a connection between python code and and MySQL we need a connector: impoty mysql.connector
connect(): this metjod is used to open or establish a new connection. it returns an object representing the connection
syntax: connection_object= connect(user='username', password='usp', host='localhost', port=3306)

Check connection: this method is used to check if connection is established with MySQL or not. Return true if connected
conn_obj= mysql.connector.connect(user='username', password='usp', host='localhost', port=330)
syntax: print(conn_obj.is_connected()

Close_connection: conn_obj.close
'''

#create connection
import mysql.connector
conn_obj= mysql.connector.connect(user='username', password='usp', host='localhost', port=330)

#to create databse:
conn_obj= mysql.connector.connect(user='username', password='usp', host='localhost', database= 'uspDB', port=330)

#To create a table in DB
table= 'CREATE TABLE student (studid int auto_increament primary key, name varchar 20, gender varchar (10))'
mycon=conn_obj.cursor()             #cursor methosd is used to run the query
mycon.execute(table)                # we need cursor method to execute this

#to fetch the row count from DB
table= 'select * from student'
mycon=conn_obj.cursor()
mycon.execute(table)
print('total rows:', mycon.rowcount)

# Fetch all rows from DB
table= 'select * from student'
mycon=conn_obj.cursor()
mycon.execute(table)
rows= mycon.fetchall()
for r  in rows:
    print(r)














