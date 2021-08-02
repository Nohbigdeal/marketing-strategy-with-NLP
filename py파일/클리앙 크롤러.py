from bs4 import BeautifulSoup
import urllib.request as req
import pandas as pd
import numpy as np
import time

url = 'https://www.clien.net/service/group/community?&od=T31&po=0'
res = req.urlopen(url)  # 소스를 res로 넣는다
soup = BeautifulSoup(res, "html.parser")

title = soup.select("div > div.list_title > span > a")
titList = []

for i in range(0, 6):
    url = "https://www.clien.net/service/search?q=%EA%B0%A4%EB%9F%AD%EC%8B%9C&p=" + str(i) + "&boardCd=&isBoard=false"
                                                # 검색어 바꾸기 (&p= 전까지)
    res = req.urlopen(url)  # 소스를 res로 넣는다
    soup = BeautifulSoup(res, "html.parser")
    title = soup.select("div > div.list_title > span > a")
    for j in range(0, len(title)):
      tit = title[j].text
      titList.append(tit)
print(titList)

data = pd.DataFrame(titList)
print(data)
data.to_csv('클리앙 건조기 타이틀.csv', header=None)