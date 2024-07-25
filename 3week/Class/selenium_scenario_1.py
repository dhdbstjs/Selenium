'''
1. 유저 시나리오 TC화 하기
CGV 홈페이지에 접속해 영화 이름 검색
존재하지 않는 영화 이름 검색
존재하지 않는 영화 검색 시 결과 페이지를 확인한다
한글 영화 이름을 검색한다
영문 영화 이름을 검색한다
특수문자가 포함된 영화 이름을 검색한다
영화 상세 정보로 이동한다
CGV 로고를 클릭하여 홈으로 이동한다

2. TC를 자동화 하기
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.cgv.co.kr')
driver.implicitly_wait(10)

# TC_001: 홈페이지 접속 확인 TRUE / FALSE
if driver.find_element(By.CSS_SELECTOR, "#cgvwrap > div.header > div.header_content > div > h1 > a > img").is_displayed():
    print("CGV")
else:
    print("CGV 접속 실패")
    print(f"url : {driver.current_url}")


# TC_002: 비유요한 영화 이름 검색
elem = driver.find_element(By.CSS_SELECTOR, "#header_keyword")
elem.click()
elem.send_keys("qwerqwer")
driver.find_element(By.CSS_SELECTOR, "#btn_header_search").click()
driver.implicitly_wait(10) # 페이지 이동하면 묵시적 대기 걸어줘야한다

if driver.find_element(By.CSS_SELECTOR, "#search_result").text == "'qwerqwer' 검색결과가 없습니다.":
    print("비유효한 영화 검색")
else:
    print("영화 검색 실패")
    print(driver.find_element(By.CSS_SELECTOR, "#search_result").text)


#TC_003: 한글 영화 이름 검색
elem = driver.find_element(By.CSS_SELECTOR, "#header_keyword")
elem.click()
elem.send_keys("토이스토리")
driver.find_element(By.CSS_SELECTOR, "#btn_header_search").click()
driver.implicitly_wait(10)

if driver.find_element(By.CSS_SELECTOR, "#searchMovieResult > ul > li > a > img").is_displayed():
    print("한글 영화 검색 성공")
else:
    print("한글 영화 검색 실패")


# TC_004: CGV 로고 버튼 기능 확인
driver.find_element(By.CSS_SELECTOR, "#cgvwrap > div.header > div.header_content > div > h1 > a > img").click()
driver.implicitly_wait(10)
if driver.current_url == "https://www.cgv.co.kr/":
    print("로고 기능 확인 성공")
else:
    print("로고 기능 확인 실패")
    print(f"current_url : {driver.current_url}")