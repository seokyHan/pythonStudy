import requests
from bs4 import BeautifulSoup

mysrc = requests.get("http://localhost/emplist")

# 파싱한 데이터
soup = BeautifulSoup(mysrc.text, 'html.parser')

# print(mysrc.text)
# print("---------------------------------------")
mytable = soup.select('table')[0]
trs = mytable.select('tr')
for idx, i in enumerate(trs):
    if idx > 0:
        tds = i.select('td')
        print(tds[0].text,end="\t")
        print(tds[1].text,end="\t")
        print(tds[2].text,end="\t")
        print(tds[3].text)