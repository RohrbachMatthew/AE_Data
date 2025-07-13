import mysql.connector
from config import db_config

try:
    connection = mysql.connector.connect(**db_config)
    print("Connection to Database Successful")
    connection.close()

except mysql.connector.Error as err:
    print("Connection Failed:", err)