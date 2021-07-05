import json
import csv
import requests
import bs4
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

columns=['position', 'name', 'games', 'goals', 'points']
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    standings=[]
    page = requests.get('https://lpf.ro/liga-1')
    soup= bs4.BeautifulSoup(page.content, features='html.parser')

    table_parent=soup.find(id='clasament_ajax_playoff')
    table=table_parent.find('table')
    table_rows=table.find_all('tr', class_='echipa_row')
    for table_row in table_rows:
        #tds=table_row.find('td')

        text_from_tds=[
            td.text for td in table_row.find_all('td')
             if 'hiddenMobile' not in td.get('class',[]) and td.text ]
        team_dict={col: data for col, data in zip(columns, text_from_tds)}
        standings.append(team_dict)
    print(standings)
    with open('standings.json',mode='w') as json_file:
        json.dump(standings, json_file, indent=2)

    with open('standings.csv', mode='w') as csv_file:
        csv_writer=csv.writer(csv_file,delimiter='_')
        csv_writer.writerow(columns)
        csv_writer.writerow([team_dict.values() for team_dict in standings])


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
