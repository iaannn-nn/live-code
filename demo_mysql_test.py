# import mysql.connector

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="password"
# )

# print(mydb)


# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="password"
# )

# mycursor = mydb.cursor()

# #mycursor.execute("CREATE DATABASE mydatabase")

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)


#try connecting to your db
# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="password",
#   database="mydatabase"
# )


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Users")

myresult = mycursor.fetchall()
print(myresult)

for x in myresult:
  print(x)


# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="password",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()

# sql = "INSERT INTO Users (name, password) VALUES (%s, %s)"
# val = ("Yen", "password")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")