import scrapy
from scrapy.http.response.html import HtmlResponse


class NavernewsSpider(scrapy.Spider):
    name = 'navernews'
    # allowed_domains = ['news.naver.com']
    # start_urls = ['http://news.naver.com/']
    
    allowed_domains = ['https://heodolf.tistory.com/18']
    start_urls = ['https://heodolf.tistory.com/18']

    def parse(self, response: HtmlResponse):
        print('====================================================================')
        print('====================================================================')
        print(response.text)
        print('====================================================================')
        print('====================================================================')
