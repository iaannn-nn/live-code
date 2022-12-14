import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("""
CREATE TABLE Sleepentry (
  user_id int,
  sleepdate DATE,
  sleeptime DATETIME,
  wakeuptime DATETIME,
  totalsleep TIME,
  FOREIGN KEY(user_id) REFERENCES Users(user_id)
)
""")