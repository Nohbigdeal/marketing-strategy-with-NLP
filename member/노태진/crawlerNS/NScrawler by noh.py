from bs4 import BeautifulSoup
from selenium import webdriver
import selenium
from urllib.parse import  urlparse
import time
import lxml
from NaverShoppingProductsCrawler import ProductCrawler
from urllib.request import urlopen
from selenium.webdriver.common.keys import Keys

names, prices, dates, reviewnum = [], [], [], []
driver = None
driver = webdriver.Chrome("chromedriver")

for i in range(5):

    URL = "https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EA%B0%A4%EB%9F%AD%EC%8B%9C&pagingIndex=" + str(i+1) +"&pagingSize=80&productSet=total&query=%EA%B0%A4%EB%9F%AD%EC%8B%9C&sort=review&timestamp=&viewType=list"

    driver.get(URL) # chrome 실행
    ###########################################################
    elem = driver.find_element_by_tag_name("body")
    no_of_pagedowns = 30
    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        no_of_pagedowns -= 1
    time.sleep(2) # Scroll down
    ###########################################################
    response = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(response, 'lxml')
    a = soup.find_all('div', class_="basicList_info_area__17Xyo")

    for n in a:
        names.append(n.find('a', class_="basicList_link__1MaTN").text) #productname   
        try:
            prices.append(str(n.find('span', class_="price_num__2WUXn").text.replace(",", "").replace("원", ""))) #price
        except:
            # n.find('span', class_="price_num__2WUXn").text.replace(",", "") = None
            prices.append("77")
        dates.append(n.find('span', class_="basicList_etc__2uAYO").text) #'등록일 20xx.xx'형식
        reviewnum.append(n.find('em', class_="basicList_num__1yXM9").text.replace(",", ""))
        if int(n.find('em', class_="basicList_num__1yXM9").text.replace(",", "")) < 10:
            break

        
print(names)
print(prices)
print(dates)
print(reviewnum)