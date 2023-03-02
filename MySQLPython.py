Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="Alex",
    password="BestPassword89"
    )
print(mydb)
<mysql.connector.connection_cext.CMySQLConnection object at 0x000001A0FD52B310>
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE myPyDatabase")
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)

    
('information_schema',)
('mypydatabase',)
('mysql',)
('performance_schema',)
('sakila',)
('sys',)
('world',)
