import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

try:
    service = ChromeService(executable_path=ChromeDriverManager().install())
    
    print(service)

    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}

    # driver = webdriver.Chrome(service=service)

    # # driver.get("http://naver.com")
    # driver.get("https://www.kogl.or.kr/recommend/recommendDivView.do?recommendIdx=39741&division=img")

    # time.sleep(10)

    # driver.page_source
except Exception as e:
    print(e)
finally:
    # driver.quit()
    print("finally")
