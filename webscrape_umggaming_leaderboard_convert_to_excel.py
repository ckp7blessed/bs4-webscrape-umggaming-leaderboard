import requests
import bs4
import xlsxwriter

url = 'https://umggaming.com/leaderboards'

res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, 'lxml')

leaderboard = soup.find('table', {'id': 'leaderboard-table'})
tbody = leaderboard.find('tbody')

players = []

for tr in tbody.find_all('tr'):
	place = tr.find_all('td')[0].text.strip()
	username = tr.find_all('td')[1].find_all('a')[1].text.strip()
	xp = tr.find_all('td')[4].text.strip()
	players.append([place, username, xp])

workbook = xlsxwriter.Workbook("C:\\Users\\Boss\\Desktop\\umggaming_leaderboard.xlsx")
worksheet = workbook.add_worksheet('Data')

bold = workbook.add_format({'bold': True})

worksheet.write('A1', 'Place', bold)
worksheet.write('B1', 'Username', bold)
worksheet.write('C1', 'XP', bold)

row = 1
col = 0

for place, name, xp in players:
	worksheet.write(row, col, place)
	worksheet.write(row, col+1, name)
	worksheet.write(row, col+2, xp)
	row += 1

workbook.close()