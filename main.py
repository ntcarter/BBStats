from basketball_reference_scraper.box_scores import get_box_scores
import DatabaseTest
import GlobalLocals


print("Beginning main")

b1 = DatabaseTest.BBalldataBase()
b1.createDataBase()
b1.connectToDb("localhost", "root", "root", "bbstats")

print("-----------------------------")
print(b1.connection)
print("-----------------------------")
print(b1.createScheduleTable())
print(b1.createBoxScoreTable())
print("-----------------------------")
print("*****************************")
# b1.createSeasonCSVFromInternet(2015, "D:/githubDesktop/BBStats/BBStats/CSVFiles/Seasons/season2015.csv")
print("*****************************")
# b1.populateScheduleFromCSV(f"{GlobalLocals.PATH_TO_CSV_FOLDER}season2021.csv")
# b1.populateScheduleFromCSV(f"{GlobalLocals.PATH_TO_CSV_FOLDER}season2020.csv")
# b1.populateScheduleFromCSV(f"{GlobalLocals.PATH_TO_CSV_FOLDER}season2019.csv")
# b1.populateScheduleFromCSV(f"{GlobalLocals.PATH_TO_CSV_FOLDER}season2018.csv")
# b1.populateScheduleFromCSV(f"{GlobalLocals.PATH_TO_CSV_FOLDER}season2017.csv")
# b1.populateScheduleFromCSV(f"{GlobalLocals.PATH_TO_CSV_FOLDER}season2016.csv")
# b1.populateScheduleFromCSV(f"{GlobalLocals.PATH_TO_CSV_FOLDER}season2015.csv")


# NEED TO CREATE CSV FOR BOX SCORES

# THEN INSERT INTO DB FROM CSV

s = get_box_scores('2020-01-13', 'CHI', 'BOS', period='GAME', stat_type='BASIC')
# s = get_box_scores('2021-02-02', 'LAC', 'BRK', period='GAME', stat_type='BASIC')
print(s.__class__)
print(s)

temp1 = s.get('BOS')
temp = s.get('CHI')

print("*********************************")
dict1 = temp1.to_dict(orient='split')
print(dict1)
print(dict1 .__class__)
print(dict1['columns'])
print("*********************************")


print("END OF MAIN")
