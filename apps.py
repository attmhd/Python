from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url = "https://www.bmkg.go.id/"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

html = urlopen(req).read()
data = BeautifulSoup(html, 'html.parser')
dataBMKG = data.find('div',{'class':'gempabumi-home-bg margin-top-13'}).text
print(dataBMKG)