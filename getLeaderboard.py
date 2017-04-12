import requests
import json
from bs4 import BeautifulSoup

page = requests.get("http://www.espn.com/golf/leaderboard?tournamentId=2700")
soup = BeautifulSoup(page.content, 'html.parser')


ary = []
name_array = soup.find_all('a', class_ = 'full-name')
uo_array = soup.find_all('td', class_ = 'relativeScore')
ts_array = soup.find_all('td', class_ = 'totalScore in post')
length = len(name_array)

for i in range(0, length):
    full_name = name_array[i].get_text()
    try:
        under_over = int(uo_array[i].get_text())
    except ValueError:
        under_over = uo_array[i].get_text()
    total_score = int((ts_array[i].get_text()))
    ary.append({'playerName': full_name, 'score': total_score, 'overUnder': under_over})
print(ary)

file = open("leaderboard_data.json", "w")
output = ary
json.dump(output, file)
file.close()
