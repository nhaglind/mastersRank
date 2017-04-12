import requests
import json
from bs4 import BeautifulSoup

page = requests.get("http://www.espn.com/golf/leaderboard")
soup = BeautifulSoup(page.content, 'html.parser')
full_name = soup.find_all('a', class_='full-name')[0].get_text()
round_1 = soup.find_all('td', class_='round1 in post')[0].get_text()
round_2 = soup.find_all('td', class_='round2 in post')[0].get_text()
round_3 = soup.find_all('td', class_='round3 in post')[0].get_text()
round_4 = soup.find_all('td', class_='round4 in post')[0].get_text()
total_score = soup.find_all('td', class_='totalScore in post')[0].get_text()

print(full_name, round_1, round_2, round_3, round_4, total_score)

file = open("leaderboard_data.json", "w")
output = {"playerName": (full_name), "score": (total_score)}
json.dump(output, file)
file.close()
