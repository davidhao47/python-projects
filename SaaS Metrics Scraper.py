import requests
import csv
from BeautifulSoup import BeautifulSoup

url = 'http://blossomstreetventures.com/blog_details.php?bcat_id=137&utm_campaign=Mattermark%20Daily&utm_source=hs_email&utm_medium=email&utm_content=53092886&_hsenc=p2ANqtz-8EhugS_OoTCWHcn5NrvA-Jm6VUjXVuab4uKZo3vlx_skDWM2sTMj_XsF_wyKzjuN5DXlGiEeM9ThIahfFYrRjQzvDWGw&_hsmi=53092886'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('tbody')


list_of_rows = []
for row in table.findAll('tr')[1:]:
	list_of_cells = []
	for cell in row.findAll('td'):
		text = cell.text.replace('&nbsp;', '')
		list_of_cells.append(text)
	list_of_rows.append(list_of_cells)
	
outfile = open("./hidan.csv","wb")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)
