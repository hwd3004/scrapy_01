import scrapy
from scrapy.http.response.html import HtmlResponse
from bs4 import BeautifulSoup


class NavernewsSpider(scrapy.Spider):
    name = 'navernews'
    # allowed_domains = ['news.naver.com']
    # start_urls = ['http://news.naver.com/']

    # allowed_domains = ['https://heodolf.tistory.com/18']
    # start_urls = ['https://heodolf.tistory.com/18']

    allowd_domins = ['https://www.kogl.or.k']
    start_urls = ['https://www.kogl.or.kr/recommend/recommendDivView.do?recommendIdx=39741&division=img']

    def parse(self, res: HtmlResponse):
        # scrapy crawl navernews
        try:
            soup = BeautifulSoup(res.text, "lxml")

            # print(soup)

            with open("temp1.html", "w", encoding="utf8") as f:
                f.write(res.text)

        except Exception as e:
            print(e)
