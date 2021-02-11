import DatabaseTest


def mainStart(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Beginning main")  # Press Ctrl+F8 to toggle the breakpoint.


mainStart("Temp")

b1 = DatabaseTest.BBalldataBase()
b1.createDataBase()
b1.connectToDb("localhost", "root", "root", "bbstats")

# b1.createSeasonCSV(2021, "PATH TO CSV HERE")

print("-----------------------------")
print(b1.connection)
print("-----------------------------")
print(b1.createScheduleTable())
print("-----------------------------")
print("*****************************")
# b1.createSeasonCSVFromInternet(2021, "PATH TO CSV HERE")
print("*****************************")
b1.populateScheduleFromCSV("tmp", "tmp", "PATH TO CSV HERE")
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
