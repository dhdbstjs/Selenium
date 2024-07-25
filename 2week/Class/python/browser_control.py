import time
from selenium import webdriver

driver = webdriver.Chrome()

# 브라우저 크기 최대화
driver.maximize_window()
time.sleep(5)

# 특정 페이지에 접속
driver.get('https://google.co.kr')

# 해당 페이지의 타이틀, url 출력
print(driver.title)
print(driver.current_url)
time.sleep(5)

# 브라우저 위치 조정
driver.set_window_position(0, 0)
time.sleep(5)

# 브라우저 크기 조정
driver.set_window_size(500,500)
time.sleep(5)

# 또 다른 페이지 접속
driver.get('https://naver.com')

# 새로 접속한 페이지 타이틀, url 출력
print(driver.title)
print(driver.current_url)
time.sleep(5)