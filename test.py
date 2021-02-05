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


s = get_schedule(2019, playoffs=True)

# all data Printed
print(s)
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
# date
print(s['data'][1][0])

# Visitor
print(s['data'][1][2])

# home
print(s['data'][1][4])
print("-----------------------------------------------------------")
