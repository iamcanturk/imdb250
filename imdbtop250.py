from bs4 import BeautifulSoup
import urllib.request
url = "http://www.imdb.com/chart/top"
url_oku= urllib.request.urlopen(url)
soup = BeautifulSoup(url_oku,'html.parser')
cek= soup.find_all('td',attrs={'class':'titleColumn'})
for i in range(0,250):
    {print(cek[i].text)}
