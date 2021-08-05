from bs4 import BeautifulSoup
from selenium import webdriver
import selenium
from urllib.parse import  urlparse
import time
import lxml
from NaverShoppingProductsCrawler import ProductCrawler
from urllib.request import urlopen
from selenium.webdriver.common.keys import Keys

driver = None
driver = webdriver.Chrome("chromedriver")

URL = "https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EA%B0%A4%EB%9F%AD%EC%8B%9C&pagingIndex=1&pagingSize=80&productSet=total&query=%EA%B0%A4%EB%9F%AD%EC%8B%9C&sort=rel&timestamp=&viewType=list"

driver.get(URL)

elem = driver.find_element_by_tag_name("body")

no_of_pagedowns = 30
while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns -= 1
time.sleep(2) #이미지 로딩 대기

response = driver.page_source.encode('utf-8')
soup = BeautifulSoup(response, 'lxml')
a = soup.find_all('li', class_="basicList_item__2XT81")

names, prices, dates, reviewnum, jjimnum = [], [], [], [], []

for n in a:
    # names.append(n.find('a', class_="basicList_link__1MaTN").text()) #productname
    # prices.append(n.find('span', class_="price_num__2WUXn").text)
    # dates.append(n.find('span', class_="basicList_etc__2uAYO").text) #'등록일 20xx.xx'형식
    # reviewnum.append(n.find('em', class_="basicList_num__1yXM9").text) #등록일 분자열 제거
    jjimnum.append(n.find_all('em', class_="basicList_num__1yXM9")) # 찜
print(jjimnum[0])
print(jjimnum[0][1])

    # print(jjimnum[1][1])
    # print(jjimnum[2][1])
    # print(jjimnum[3][1])
    
# def getProductNames(self, soup):
#     names = []
#     for product in soup :
#         names.append(product.find('a', class_="basicList_link__1MaTN").text)

#     return names

# dates = []
# for product in soup :
#     date_raw = []
#     dates.append(soup.find_all('span', class_="basicList_etc__2uAYO")) #등록일 분자열 제거
#     date_raw = product.find_all('span', class_="basicList_etc__2uAYO")
#     for n in date_raw:
#         dates.append(date_raw.find)
# print(dates)


#     def getCrawlling(self, kword, pagecount = 1):
#         URL = "https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EA%B0%A4%EB%9F%AD%EC%8B%9C&pagingIndex=2&pagingSize=80&productSet=total&query=%EA%B0%A4%EB%9F%AD%EC%8B%9C&sort=rel&timestamp=&viewType=list"

#         response = self.driver.page_source.encode('utf-8')
#         soup = BeautifulSoup(response, 'lxml')

#         return self.getContext(soup, pagecount)

# if __name__ == "__main__" :
#     crawler = ProductCrawler()
#     print(crawler.getCrawlling("갤럭시"))
#     time.sleep(20)