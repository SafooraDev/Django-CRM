import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='S@f00rA!!'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")
