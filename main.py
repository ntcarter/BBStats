import sys
import DatabaseTest
from platform import python_version
from basketball_reference_scraper.box_scores import get_box_scores


print(sys.version)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

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
