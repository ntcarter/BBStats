import mysql.connector
from mysql.connector import Error
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import GlobalLocals
import csv


# Connects to or creates an instance of the database and handles database queries

class BBalldataBase:
    connection = None

    def __init__(self):
        self.connection = None

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
            tmpConnection = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="root"
            )
            myCursor = tmpConnection.cursor()
            myCursor.execute("CREATE DATABASE IF NOT EXISTS bbStats")
        except Error as e:
            print(f"The error '{e}' occurred")

    def createScheduleTable(self):
        query = "CREATE TABLE IF NOT EXISTS schedule (" \
                "_id INTEGER NOT NULL AUTO_INCREMENT," \
                "datePlayed VARCHAR(25), " \
                "startTime VARCHAR(25)," \
                "visitor VARCHAR(50)," \
                "visitorPts VARCHAR(10)," \
                "home VARCHAR(50)," \
                "homePts VARCHAR(10)," \
                "numOT VARCHAR(5)," \
                "PRIMARY KEY (_id) )"
        try:
            myCursor = self.connection.cursor()
            myCursor.execute(query)
        except Error as e:
            print(f" .createScheduleTable: The error '{e}' occurred")

    # gets the schedule data from the link in the function
    def get_schedule(self, season):
        # all months the NBA has games
        months = ['October', 'November', 'December', 'January', 'February', 'March',
                  'April', 'May', 'June']
        df = pd.DataFrame()
        for month in months:
            t = f'https://www.basketball-reference.com/leagues/NBA_{season}_games-{month.lower()}.html'
            # need google chrome and chromium and chrome driver to run code. Get chromium here:
            # https://chromedriver.chromium.org/downloads
            driver = webdriver.Chrome(GlobalLocals.PATH_TO_CHROMIUM)
            # downloads the html and renders the JS
            driver.get(t)
            html = driver.page_source
            if html is not None:
                soup = BeautifulSoup(html, 'html.parser')
                # Look for the h1 tag which holds page not found text if the NBA didn't play that month
                checkHeader = soup.find('h1')
                if checkHeader.contents[0] != "Page Not Found (404 error)":
                    table = soup.find('table', attrs={'id': 'schedule'})
                    month_df = pd.read_html(str(table))[0]
                    df = df.append(month_df)

        # returns the season data in a pandas DataFrame
        return df

    def insertIntoDB(self, dbReader):

        for row in dbReader:
            # replace empty data with NaN
            if row[8] == "":
                row[8] = "NaN"
            if row[4] == "":
                row[4] = "NaN"
            if row[6] == "":
                row[6] = "NaN"
            if row[1] != "Date" and row[1] != "Playoffs":
                query = "INSERT INTO bbstats.schedule (datePlayed, startTime, visitor, visitorPts, home, homePts, numOT)" \
                        f" VALUES('{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}', '{row[6]}', '{row[8]}')"
                try:
                    myCursor = self.connection.cursor()
                    myCursor.execute(query)
                    self.connection.commit()
                except Error as e:
                    print(f" .insertIntoDB: The error '{e}' occurred")
                    print(f"Error: {row[8]}")

    # takes the input CSV and inserts it into the schedule database
    # This function assumes that the database has a valid schedule table
    def populateScheduleFromCSV(self, CSVPath):
        # Try to open the CSV. If successful parse each row of the CSV and insert into the Schedule database
        try:
            with open(f'{CSVPath}') as csvFile:
                reader = csv.reader(csvFile, delimiter=',')
                self.insertIntoDB(reader)
        except Error as e:
            print(f"ERROR: populateScheduleFromCSV the error '{e}' occured")

    # downloads a schedule and creates a csv file at path pathToCSVFile
    def createSeasonCSVFromInternet(self, seasonEndYear, pathToCSVFile):
        df = self.get_schedule(seasonEndYear)
        try:
            df.to_csv(r'{}'.format(pathToCSVFile))
        except Error as e:
            print(f" .createScheduleTable: The error '{e}' occurred")
