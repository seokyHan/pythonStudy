from bs4 import BeautifulSoup
import requests, datetime
from daostock import DaoStock


mysrc = requests.get("https://vip.mk.co.kr/newSt/rate/item_all.php")
mysrc.encoding = 'euc-kr'
# 파싱한 데이터
soup = BeautifulSoup(mysrc.text, 'html.parser')
now = datetime.datetime.now()
nowDatetime = now.strftime('%Y%m%d_%H%M')

sts = soup.select('.st2')
de = DaoStock()

for st2 in sts:
    myparent = st2.parent
    tds = myparent.select('td')
    s_name = tds[0].text
    s_code = tds[0].a['title']
    price = tds[1].text.replace(",","")
    ymd_hm = nowDatetime
    
    de.myinsert(s_code, s_name, price, ymd_hm)
    print("긁어오기 성공!")
    
    
