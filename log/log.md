python version 3.10

---

pipenv install scrapy selenium

pipenv install webdriver-manager

---

scrapy startproject main .

scrapy genspider navernews news.naver.com - 이름이 navernews인 spider를 spiders 폴더에 생성

scrapy crawl navernews - Spider 실행 확인
