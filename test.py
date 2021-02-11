import pandas as pd
from requests import get
from bs4 import BeautifulSoup

print("begin")


# get the schedule from the link in the fucntion
def get_schedule(season, playoffs=False):
    months = ['October', 'November', 'December', 'January', 'February', 'March',
              'April', 'May', 'June']
    df = pd.DataFrame()
    for month in months:
        t = f'https://www.basketball-reference.com/leagues/NBA_{season}_games-{month.lower()}.html'
        r = get(t)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'html.parser')
            table = soup.find('table', attrs={'id': 'schedule'})
            month_df = pd.read_html(str(table))[0]
            df = df.append(month_df)
    df = df.to_dict(orient='split')
    return df


s = get_schedule(2021, playoffs=True)

# all data Printed
print(s)
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("Trying to get number of iterations:")
indexLength = s['data']
print("Length: ")
for val in indexLength:
    print(val)
# date
print(s['data'][0][0])
#Start Time
print(s['data'][0][1])
# Visitor
print(s['data'][0][2])
#Visitor Points
print(s['data'][0][3])
# home
print(s['data'][0][4])
#home Points
print(s['data'][0][5])
#num OT
print(s['data'][0][7])
print("-----------------------------------------------------------")
