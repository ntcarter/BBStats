import DatabaseTest
import GlobalLocals

def mainStart(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Beginning main")  # Press Ctrl+F8 to toggle the breakpoint.


mainStart("Temp")

b1 = DatabaseTest.BBalldataBase()
b1.createDataBase()
b1.connectToDb("localhost", "root", "root", "bbstats")

print("-----------------------------")
print(b1.connection)
print("-----------------------------")
print(b1.createScheduleTable())
print("-----------------------------")
print("*****************************")
# b1.createSeasonCSVFromInternet(2015, "D:/githubDesktop/BBStats/BBStats/CSVFiles/season2015.csv")
print("*****************************")
b1.populateScheduleFromCSV(f"{GlobalLocals.PATH_TO_CSV_FOLDER}season2021.csv")
b1.populateScheduleFromCSV(f"{GlobalLocals.PATH_TO_CSV_FOLDER}season2020.csv")
b1.populateScheduleFromCSV(f"{GlobalLocals.PATH_TO_CSV_FOLDER}season2019.csv")
b1.populateScheduleFromCSV(f"{GlobalLocals.PATH_TO_CSV_FOLDER}season2018.csv")
b1.populateScheduleFromCSV(f"{GlobalLocals.PATH_TO_CSV_FOLDER}season2017.csv")
b1.populateScheduleFromCSV(f"{GlobalLocals.PATH_TO_CSV_FOLDER}season2016.csv")
b1.populateScheduleFromCSV(f"{GlobalLocals.PATH_TO_CSV_FOLDER}season2015.csv")
print("END OF MAIN")

# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# print(python_version())
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
# # s = get_box_scores('2020-01-13', 'CHI', 'BOS', period='GAME', stat_type='BASIC')
# s = get_box_scores('2021-02-02', 'LAC', 'BRK', period='GAME', stat_type='BASIC')
# print(s.__class__)
# print(s)
#
# # temp1 = s.get('BOS')
# # temp = s.get('CHI')
#
# # print("*********************************")
# # dict1 = temp1.to_dict(orient='split')
# # print(dict1)
# # print(dict1 .__class__)
# # print(dict1['columns'][3])
# # print("*********************************")
#
