import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.cgv.co.kr')
driver.implicitly_wait(10)
# implicitly_wait는 묵시적 대기! 밑에 코드에 오류가 없는데 네트워크 요소때문에 페이지에 접속되는 대기 시간을 주는 것!
# implicitly_wait : 페이지가 로딩될 떄까지 기다림 / 로딩되면 코드 실행 / 로딩 실패하면 오류 발생
# time_sleep : 페이지 로딩 여부 상관 없이 n초 기다림 / 로딩 되지 않아도 코드 실행
# 이 둘은 필요한 상황이 다르다!

elem = driver.find_element(By.CSS_SELECTOR, '#btn_allView_Movie')

print(elem.get_attribute('id'))
print(elem.text)
print(elem.location)
elem.screenshot('./cgv_logo.png')

# 엘리먼트 요소 / 애트리뷰트 속성