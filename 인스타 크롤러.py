from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import csv
import pandas as pd
import urllib
import ssl
import random


search = input('검색어 : ')
search1 = urllib.parse.quote(search)
url = 'https://www.instagram.com/explore/tags/'+str(search1)+'/'

driver = webdriver.Chrome('C:/3pm/pythonwork/analysis/chromedriver/chromedriver') # 크롬드라이버 위치 수정
driver.implicitly_wait(1)
driver.get(url)
time.sleep(20)

driver.get(url)
time.sleep(5)
driver.find_element_by_class_name('eLAPa').click()

time.sleep(2)

with open(search+'인스타댓글.csv', 'a', newline='', encoding='utf-8') as out:
    writer = csv.writer(out)
    replylist = []
    for temp in range(0,3):
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        #result = soup.find_all('a', {'class': 'xil3i'})  #해시태그가 있는 클래스
        rdata = soup.find_all('div', {'class': 'C4VMK'})  #댓글이 있는 클래스

        if len(rdata) > 0:  #댓글이 있으면
            hstr = ''   #게시글 하나의 댓글을 하나의 문장으로 저장한다.
            rresult = []
            for temp1 in rdata:
                temp1 = temp1.find_all('span')[1]
                print(temp1)
                hstr = hstr + ' ' + temp1.text
            replylist.append(hstr)
            rresult.append(hstr)

            datelist = list()
            time_raw = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > div.k_Q0X.I0_K8.NnvRN > a > time')
            time_info = pd.to_datetime(time_raw.get_attribute('datetime')).normalize()
            datelist.append(time_info)
            print(datelist)

            writer.writerow(datelist + rresult)
        driver.find_element_by_link_text('다음').click()  #다음 클릭
        time.sleep(2) #로딩이 느리면 시간을 좀 늘려주기 #봇으로 인식하는걸 막기 위해 랜덤으로 넣어줌
            #random.randint(3,10)

print(search1)
print(replylist)
print(datelist)

