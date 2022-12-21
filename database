import mysql.connector

mydb = mysql.connector.connect(
       host="192.168.43.97",
       user="Nilanjan",
       password="itripamrit",
       database="VIZION"

)
a = mydb.cursor()
#a.execute("CREATE DATABASE VIZION")
a.execute("CREATE TABLE UserAttendance (Date VARCHAR(30),USERNAME VARCHAR(255),DateTime VARCHAR(255), PRIMARY KEY (Date,USERNAME))")
#sql = "DROP DATABASE VIZION"
#a.execute(sql)
mydb.commit()
mydb.close()
