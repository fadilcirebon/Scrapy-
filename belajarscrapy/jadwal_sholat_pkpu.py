import bs4
import requests

url = 'https://jadwalsholat.org/jadwal-sholat/monthly.php?id=63'
contents = requests.get(url)

response = bs4.BeautifulSoup(contents.text, 'html.parser')
data = response.find_all('tr', 'table_highlight')
data = data[0]

sholat = {}
i = 0
for d in data:
    if i == 1:
        sholat['imsyak'] = d.get_text()
    if i == 2:
        sholat['subuh'] = d.get_text()
    elif i == 3:
        sholat['terbit'] = d.get_text()
    elif i == 4:
        sholat['dhuha'] = d.get_text()
    elif i == 5:
        sholat['zuhur'] = d.get_text()
    elif i == 6:
        sholat['ashar'] = d.get_text()
    elif i == 7:
        sholat['maghrib'] = d.get_text()
    elif i == 8:
        sholat['isya'] = d.get_text()

    i += 1

print(sholat)
print(sholat['ashar'])

