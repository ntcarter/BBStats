import mysql.connector
from mysql.connector import Error


class BBalldataBase:

    connection = None

    def __init__(self):
        self.connection = None

    def myFunc(self):
        print("Hello my name is")

    def connectToDb(self, hostName, userName, passWord, dbName):
        try:
            myConnection = mysql.connector.connect(
                host=hostName,
                user=userName,
                passwd=passWord,
                database=dbName
            )
            self.connection = myConnection
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

    def createDataBase(self):
        try:
            myCursor = self.connection.cursor()
            myCursor.execute("CREATE DATABASE IF NOT EXISTS bbStats")
        except Error as e:
            print(f"The error '{e}' occurred")

    def createScheduleTable(self):
        query = "CREATE TABLE IF NOT EXISTS schedule (" \
                "_id INTEGER NOT NULL AUTO_INCREMENT, date DATE, " \
                "startTime VARCHAR(25)," \
                "visitor VARCHAR(50)," \
                "visitorPts Integer," \
                "home VARCHAR(50)," \
                "homePts INTEGER," \
                "numOT INTEGER," \
                "PRIMARY KEY (_id) )"
        try:
            myCursor = self.connection.cursor()
            myCursor.execute(query)
        except Error as e:
            print(f" .createScheduleTable: The error '{e}' occurred")
