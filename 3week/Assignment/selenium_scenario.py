#1. CGV가 아닌 다른 웹 페이지를 대상으로 자동화 테스트 시나리오를 작성하기.
#2. 자동화 테스트 시나리오를 원하는 도구를 이용해 엑셀 등 파일에 TC화 하기.
#3. TC를 Selenium으로 자동화 하기.
#4. 작성한 시나리오와 TC파일, 자동화 코드 파일을 과제 진행 시 어려웠던 점과 함께 작성하여 제출하기.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.naver.com/')
driver.implicitly_wait(10)

# TC_001: NAVER 홈페이지 접속 확인하기
if driver.current_url == 'https://www.naver.com/':
    print("NAVER 접속 성공")
else:
    print("NAVER 접속 실패")
    print(f"url : {driver.current_url}")

# TC_002: 검색창에 "날씨" 검색
elem_search = driver.find_element(By.CSS_SELECTOR, "#query")
elem_search.click()
elem_search.send_keys("날씨")
driver.find_element(By.CSS_SELECTOR, "#search-btn").click()
driver.implicitly_wait(10)

# TC_003: 제대로 날씨 정보가 뜨는지 확인하기
if driver.find_element(By.CSS_SELECTOR, "#main_pack > section.sc_new.cs_weather_new._cs_weather > div > div:nth-child(1) > div.content_wrap > div.open > div:nth-child(2)").is_displayed():
    print("날씨 검색 성공")
else:
    print("날씨 검색 실패")

# TC_004: 날씨와 비슷한 단어로 오타를 검색
elem_search = driver.find_element(By.CSS_SELECTOR, "#nx_query")
elem_search.click()
elem_search.clear()
elem_search.send_keys("날씻")
driver.find_element(By.CSS_SELECTOR, "#nx_search_form > fieldset > button > i").click()
driver.implicitly_wait(10)

# TC_005: 날씨로 검색한 결과입니다. 날씻 검색결과 보기 라는 문구가 뜨는지 확인
if driver.find_element(By.CSS_SELECTOR, "#main_pack > section.sc_new.sp_nkeyword._slog_visible > div > div > div").is_displayed():
    print("오타 검색 성공")
else:
    print("오타 검색 실패")

# TC_006: 네이버 로고 클릭 시 홈으로 이동하는지 확인
driver.find_element(By.CSS_SELECTOR, "#header_wrap > div > div.gnb_wrap > div.header_group > div > h1 > a > img").click()
driver.implicitly_wait(10)
if driver.current_url == "https://www.naver.com/":
    print("로고 기능 확인 성공")
else:
    print("로고 기능 확인 실패")
    print(f"current_url : {driver.current_url}")

time.sleep(5)