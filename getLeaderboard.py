import requests
import json
from bs4 import BeautifulSoup

page = requests.get("http://www.espn.com/golf/leaderboard?tournamentId=2700")
soup = BeautifulSoup(page.content, 'html.parser')
full_name = soup.find_all('a', class_ = 'full-name')[0].get_text()
under_over = int(soup.find_all('td', class_ = 'relativeScore')[0].get_text())
round_1 = int(soup.find_all('td', class_ = 'round1 in post')[0].get_text())
round_2 = int(soup.find_all('td', class_ = 'round2 in post')[0].get_text())
round_3 = int(soup.find_all('td', class_ = 'round3 in post')[0].get_text())
round_4 = int(soup.find_all('td', class_ = 'round4 in post')[0].get_text())
total_score = int(soup.find_all('td', class_ = 'totalScore in post')[0].get_text())

print(full_name, round_1, round_2, round_3, round_4, total_score, under_over)

file = open("leaderboard_data.json", "w")
output = {
    "playerName": (full_name),
    "score": (total_score),
    "underOver": (under_over)
}
json.dump(output, file)
file.close()
