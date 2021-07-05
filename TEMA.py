import json

import bs4
import requests

columns=['position', 'name', 'MJ', 'V', 'I', 'points']
standings=[]
page = requests.get('https://baschet.ro/liga-nationala-de-baschet-masculin/clasament')
soup = bs4.BeautifulSoup(page.content, features='html.parser')

table_parent=soup.find(id='total')
table=table_parent.find('table')
table_rows1=table.find_all('tr')

for table_row1 in table_rows1:
    text_from_tds=[
        td.text for td in table_row1.find_all('td')
        if 'points' not in td.get('class',[]) and td.text
    ]
    team_dict1={col: data for col, data in zip(columns, text_from_tds)}
    standings.append(team_dict1)

print(standings)

with open('basketball.json', mode='w') as json_file:
    json.dump(standings, json_file, indent=2)
