import requests
from bs4 import BeautifulSoup

mysrc = requests.get("https://vip.mk.co.kr/newSt/rate/item_all.php")
mysrc.encoding = 'euc-kr'
# 파싱한 데이터
soup = BeautifulSoup(mysrc.text, 'html.parser')
print("---------------------------------------")

# 형제 선택자 방식
# name = soup.select('.st2')
# trs = soup.select('.st2 + td')
# for idx, i in enumerate(name):
#     print(name[idx].text, "----------", trs[idx].text)
# print("---------------------------------------")

# 부모 선택자 방식
sts = soup.select('.st2')
for st2 in sts:
    myparent = st2.parent
    tds = myparent.select('td')
    s_name = tds[0].text
    s_code = tds[0].a['title']
    price = tds[1].text
    
    print(s_name.ljust(10), "\t", s_code, "\t", price)
    
    
    
