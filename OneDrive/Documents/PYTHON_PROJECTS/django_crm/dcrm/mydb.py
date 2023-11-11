from mysql import connector


DB = connector.connect(host="localhost", user="root", password="itumo7290")

cursorObject = DB.cursor()

# create database

cursorObject.execute("CREATE DATABASE elderco")
print("all done")
