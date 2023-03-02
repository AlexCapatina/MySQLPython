Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="Alex",
    password="BestPassword89",
    database="myPyDatabase"
    )

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)

  
('customers',)
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
1 record inserted.
val = [
    ('Alex', "Address 1'),
     
SyntaxError: unterminated string literal (detected at line 2)
val = [
    ('Alex 1', 'Address 1'),
    ('Alex 2', 'Address 2'),
    ('Alex 3', 'Address 3'),
    ('Alex 4', 'Address 4'),
    ('Alex 5', 'Address 5'),
    ('Alex 6', 'Address 6')
    ]
     
mycursor.executemany(sql, val)
     
mydb.commit()
     
print(mycursor.rowcount, "was inserted.")
     
6 was inserted.

print("1 record inserted, ID:", mycursor.lastrowid)
     
1 record inserted, ID: 2
mycursor.execute("SELECT * FROM customers")
     
myresult = mycursor.fetchall()
     
for x in myresult:
  print(x)

     
('John', 'Highway 21', 1)
('Alex 1', 'Address 1', 2)
('Alex 2', 'Address 2', 3)
('Alex 3', 'Address 3', 4)
('Alex 4', 'Address 4', 5)
('Alex 5', 'Address 5', 6)
('Alex 6', 'Address 6', 7)
mycursor.execute("SELECT name, address FROM customers")
     
myresult = mycursor.fetchall()
     
for x in myresult:
  print(x)

     
('John', 'Highway 21')
('Alex 1', 'Address 1')
('Alex 2', 'Address 2')
('Alex 3', 'Address 3')
('Alex 4', 'Address 4')
('Alex 5', 'Address 5')
('Alex 6', 'Address 6')
mycursor.execute("SELECT * FROM customers")
     
myresult = mycursor.fetchone()
     
print(myresult)
     
('John', 'Highway 21', 1)
