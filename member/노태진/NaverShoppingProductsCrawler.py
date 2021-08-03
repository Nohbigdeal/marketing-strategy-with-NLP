from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import  urlparse
import time


class ProductCrawler :
    driver = None

    def __init__(self):

        self.driver = webdriver.Chrome("chromedriver")
        self.driver.implicitly_wait(2)

    def __del__(self):
        self.driver.close()

    def getProducts(self, soup):
        return soup.find_all(class_="_model_list _itemSection")

#-----------------------------------------------------------------------
    def getNv_mids(self, soup):
        nv_mid = []
        for product in soup :
            nv_mid.append(product['data-nv-mid'])

        return nv_mid

    def getProductNames(self, soup):
        names = []
        for product in soup :
            names.append(product.find(class_="basicList_link__1MaTN").text)

# <a target="_blank" class="basicList_link__1MaTN" rel="noopener" data-nclick="N=a:lst*N.title,i:27435650070,r:82" title="[갤럭시] 삼성 갤럭시Z플립 256G SM-F700 미개통 미개봉 새제품" href="https://cr.shopping.naver.com/adcr.nhn?x=qHDI1szkE7mb7258JMRMkv%2F%2F%2Fw%3D%3Ds4WDzJ2bOZSdX9ZnGFxZ1mnIrSTmrPGyDjn9u%2BiQ5k%2By9BoQz4IoS1PsOnkuwjJ%2F8KdhSJ83pbUNRN5LLOQoIJTx51D3SeVSPWUXyD0rUZ4VIbemqNkkI2JLf98Kc7SitslGUX9zTlMrygskz3%2BS0g9%2B5CcYT6i7R71k9hGw5oerHaRPVsse2J3%2FKtbqGlV34s4PxzUzI2Oc23YAEU0dtMRGFggpqnm34xLi6IAYCT6w6rUqH34xyiEN%2BFtoyv5OJ%2F6Ko6CiZ1dJA1DjEv7D5%2BLIjapMN0PmuS7eneebUYVyi4%2Fr0lz1oSk9AW8qzFsUvpOr9sPYwajBkeE07IGGkJ5SCPsmGKllbt0kl8XIxCXQXw5qXIq3ch3OlPgZESUUOWl3oeQXg%2BWtXJGNPVh9NbIEEwGhxuXoG%2BJrsM3G0TjpobH4NET9Pcu1jaAnBZOEowwmx%2FZMx38HHoKh3UJYvVFKE98jZnuuxujk8XUyWXZ72mTFPN4zeb0M%2FqrH6Eyy5Syhiie3jSq89GYPm2X8XEdyHOGX7qfCiJKTRWOuR9dOim8JxdZ%2FhM7MVW9dOXPYYztH93wGYfGHsa6UofZDwa8Aq3pkHEljDrqW%2FT%2FD5EnU8TN1EqEHK6bJ9cR6R%2FHf%2BLYGwrul9chVgCxloYgdFXJvkzL99wqS7eV%2BnF7v3g%2B%2FtBMvR3xEVxSAJnlXiEXyAhWw3%2BIByOa0jCVNQVnCDoA%3D%3D&amp;nvMid=27435650070&amp;catId=50000249">[갤럭시] 삼성 갤럭시Z플립 256G SM-F700 미개통 미개봉 새제품</a>

        return names


    def getDates(self, soup):
        dates = []
        for product in soup :
            dates.append(product.find(class_="basicList_etc__2uAYO").text[4:]) #등록일 분자열 제거

        return dates

    def getPrices(self, soup):
        nv_mid = []
        for product in soup :
            try :
                price_text = product.find(class_="price_num__2WUXn").text
                price_text = str(price_text).replace(",", "")
            except AttributeError as e :
                price_text = "판매 중지"
                print(e)
                nv_mid.append(price_text)
                continue

            nv_mid.append(price_text)

        return nv_mid

#----------------------------------------------------------

    # def getProductImgsUrl(self, soup):
    #     imgs = []
    #     for product in soup :
    #         imgs.append(product.find(class_="_productLazyImg")['data-original'])

    #     return imgs


    # def setProductSort(self):
    #     self.driver.find_element_by_css_selector("#basic_List_num_").click() # 리뷰 많은순
    #     self.driver.find_element_by_css_selector("#_sort_date").click() # 등록일순
    #     time.sleep(2)

    def goPage(self, pageindex):
        # self.driver.execute_script("shop.detail.ReviewHandler.page(" + str(i) + ", '_review_paging');")
        # self.driver.execute_script("shop.search.loader.goPage(" + str(pageindex) + ", '_result_paging');")
        time.sleep(2) # 이미지 로딩 대기

    def getUrlParsed(self, URL):
        url = urlparse(URL)
        return url.query.split("&")[0].split("=")[1]  # nvMid 값을 추출함


    def getContext(self, soup, pageIndex = None) :
        if pageIndex is None :
            pageIndex = 3

        nv_mids, names, prices, dates, img_urls = [], [], [], [], []

        for page in range(1, pageIndex+1):

            response = self.driver.page_source.encode('utf-8')
            soup = BeautifulSoup(response, 'lxml')

            products = self.getProducts(soup) # get review divs

            nv_mids += self.getNv_mids(products)
            names += self.getProductNames(products)
            prices += self.getPrices(products)
            dates += self.getDates(products)
            # img_urls += self.getProductImgsUrl(products)

            if page != pageIndex :
                self.goPage(page)


        return nv_mids, names, prices, dates, img_urls

    def getCrawlling(self, kword, pagecount = 1):
        URL = "https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=" + kword + "&pagingIndex=" + str(pagecount) + "&pagingSize=80&productSet=total&query=" + kword + "&sort=rel&timestamp=&viewType=list"

        self.driver.get(URL)
        # self.setProductSort() #리뷰 많은순 정렬
        time.sleep(2) #이미지 로딩 대기

        response = self.driver.page_source.encode('utf-8')
        soup = BeautifulSoup(response, 'lxml')

        return self.getContext(soup, pagecount)

if __name__ == "__main__" :
    crawler = ProductCrawler()
    print(crawler.getCrawlling("갤럭시"))
    time.sleep(20)

# crawler = ProductCrawler()
# crawler.getCrawlling("https://search.shopping.naver.com/search/all?query=%EA%B0%A4%EB%9F%AD%EC%8B%9C&cat_id=&frm=NVSHATC")
# https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=갤럭시&pagingIndex=1&pagingSize=80&productSet=total&query=갤럭시&sort=rel&timestamp=&viewType=list
# https://search.shopping.naver.com/search/category?cat_id=   https://search.shopping.naver.com/search/all?query=갤럭시&cat_id=&frm=NVSHATC
# https://search.shopping.naver.com/search/category?cat_id=   https://search.shopping.naver.com/search/all?query=%EA%B0%A4%EB%9F%AD%EC%8B%9C&cat_id=&frm=NVSHATC
# https://search.shopping.naver.com/search/category?cat_id=50000003