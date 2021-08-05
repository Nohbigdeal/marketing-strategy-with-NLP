from bs4 import BeautifulSoup
from selenium import webdriver
import selenium
from urllib.parse import  urlparse
import time
import lxml
from urllib.request import urlopen
from selenium.webdriver.common.keys import Keys
import numpy as np
import pandas as pd

# for word in ["갤럭시", "버즈라이브", "버즈플러스", "갤탭", "갤럭시북", "갤럭시기어"]:
# for word in ["맥북", "M1", "아이폰", "에어팟", "애플워치", "아이패드"]:
word = "맥북"
# for word in ["홍미노트", "샤오미워치", "어메이즈핏", "샤오미폰", "샤오미휴대폰"]:

keyword = word  # str
page = 20 # int 입력

names, prices, dates, reviewnum = [], [], [], []
driver = None
driver = webdriver.Chrome("chromedriver")

for i in range(page):

    URL = "https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=" + keyword + "&pagingIndex=" + str(i+1) +"&pagingSize=80&productSet=total&query=" + keyword + "&sort=review&timestamp=&viewType=list"

    driver.get(URL) # chrome 실행
    ###########################################################
    elem = driver.find_element_by_tag_name("body")
    no_of_pagedowns = 30 #count of scroll down, =30
    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        no_of_pagedowns -= 1
    time.sleep(1) # Scroll down
    ###########################################################
    response = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(response, 'lxml')
    a = soup.find_all('div', class_="basicList_info_area__17Xyo")

    for n in a:
        # if int(n.find('em', class_="basicList_num__1yXM9").text.replace(",", "")) < 10:
        #     break
        names.append(n.find('a', class_="basicList_link__1MaTN").text) #productname   
        try:
            prices.append(str(n.find('span', class_="price_num__2WUXn").text.replace(",", "").replace("원", ""))) #price
        except:
            prices.append("77") # 가격 없음 or 판매 중지일 경우 77
        dates.append(n.find('span', class_="basicList_etc__2uAYO").text) #'등록일 20xx.xx'형식
        reviewnum.append(n.find('em', class_="basicList_num__1yXM9").text.replace(",", ""))
    if reviewnum[-1] < 10:
        break

# print(names)
# print(prices)
# print(dates)
# print(reviewnum)
arr = np.vstack([np.array(names), np.array(prices), np.array(dates), np.array(reviewnum)])
df = pd.DataFrame(arr).T
print(df)
df.to_csv("C:/Users/" + keyword + str(page) + "page.csv")