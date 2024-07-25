#1. 3주차 과제로 제출한 테스트에 예외처리 하기.
#2. 3주차 과제로 제출한 내용의 테스트 결과 리포트를 txt 파일로 만들 수 있도록 구현하기.
#- 결과 리포트의 구성은 직접 구성해 보세요!


import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    # 현재 시간 구하기
    now = time.strftime('%Y_%m_%d_%Hh_%Mm')

    result_pass_list = [] # 성공한 TC 담는 리스트
    result_fail_list = [] # 실패한 TC 담는 리스트
    fail_reason_list = [] # 실패한 이유 담는 리스트
    tc_count = 4

    # 테스트 리포트 파일이 저장될 폴더 만들기
    if not os.path.exists('test_result'):
        os.makedirs('test_result')

    # 언제 실행됐는지 알기위해
    f = open(f'./test_result/{now}_Test_report.txt', 'w')

    driver = webdriver.Chrome()
    driver.get('https://www.naver.com/')
    driver.implicitly_wait(10)


    # TC_001: NAVER 홈페이지 접속 확인하기
    try:
        tc_id = "TC_001"
        if driver.current_url == 'https://www.naver.com/':
            print("NAVER 접속 성공")
            result_pass_list.append(tc_id)
        else:
            print("NAVER 접속 실패")
            print(f"url : {driver.current_url}")
            result_fail_list.append(tc_id)
            fail_reason_list.append("NAVER 접속 실패.")

    except Exception as e:
        print(f"TC_001번 테스트 수행 오류 발생 >>> {e}")


    # TC_002: 검색창에 "날씨" 검색, 제대로 날씨 정보가 뜨는지 확인하기
    try:
        tc_id = "TC_002"
        elem_search = driver.find_element(By.CSS_SELECTOR, "#query")
        elem_search.click()
        elem_search.send_keys("날씨")
        driver.find_element(By.CSS_SELECTOR, "#search-btn").click()
        driver.implicitly_wait(10)

        if driver.find_element(By.CSS_SELECTOR, "#main_pack > section.sc_new.cs_weather_new._cs_weather > div > div:nth-child(1) > div.content_wrap > div.open > div:nth-child(2)").is_displayed():
            print("날씨 검색 성공")
            result_pass_list.append(tc_id)
        else:
            print("날씨 검색 실패")
            result_fail_list.append(tc_id)
            fail_reason_list.append("날씨 검색 실패")

    except Exception as e:
        print(f"TC_002번 테스트 수행 오류 발생 >>> {e}")


    # TC_003: 날씨와 비슷한 단어로 오타를 검색, 날씨로 검색한 결과입니다. 날씻 검색결과 보기 라는 문구가 뜨는지 확인
    try:
        tc_id = "TC_003"
        elem_search = driver.find_element(By.CSS_SELECTOR, "#nx_query")
        elem_search.click()
        elem_search.clear()
        elem_search.send_keys("날씻")
        driver.find_element(By.CSS_SELECTOR, "#nx_search_form > fieldset > button > i").click()
        driver.implicitly_wait(10)

        if driver.find_element(By.CSS_SELECTOR, "#main_pack > section.sc_new.sp_nkeyword._slog_visible > div > div > div").is_displayed():
            print("오타 검색 성공")
            result_pass_list.append(tc_id)
        else:
            print("오타 검색 실패")
            result_fail_list.append(tc_id)
            fail_reason_list.append("오타 검색 실패")

    except Exception as e:
        print(f"TC_003번 테스트 수행 오류 발생 >>> {e}")

    # TC_004: 네이버 로고 클릭 시 홈으로 이동하는지 확인
    try:
        tc_id = "TC_004"
        driver.find_element(By.CSS_SELECTOR, "#header_wrap > div > div.gnb_wrap > div.header_group > div > h1 > a > i").click()
        driver.implicitly_wait(10)

        if driver.current_url == "https://www.naver.com/":
            print("로고 기능 확인 성공")
            result_pass_list.append(tc_id)
        else:
            print("로고 기능 확인 실패")
            print(f"current_url : {driver.current_url}")
            result_fail_list.append(tc_id)
            fail_reason_list.append("로고 기능 확인 실패")

        time.sleep(5)

    except Exception as e:
        print(f"TC_004번 테스트 수행 오류 발생 >>> {e}")

except Exception as e:
    print(f'테스트 실행 실패! >>> {e}')




# 통계 작성

f.write(f"테스트 수행 일자 : {now}\n")
f.write("\n[RESULT - PASS]\n")

for pass_cnt in range(len(result_pass_list)):
    f.write(f"{result_pass_list[pass_cnt]}\n")

f.write("\n[RESULT - FAIL]\n")

for fail_cnt in range(len(result_fail_list)):
    f.write(f"{result_fail_list[fail_cnt]}\n")
    f.write(f"\t{fail_reason_list[fail_cnt]}\n")

f.write("\n==========================\n\n")
f.write(f"PASS TC COUNT : {len(result_pass_list)}\n")
f.write(f"FAIL TC COUNT : {len(result_fail_list)}\n")
f.write(f"COMPLETED TEST COUNT : {len(result_pass_list) + len(result_fail_list)}\n")
# 수행한 TC 개수 / 전체 TC 개수 * 100
f.write(f'PROGRESS OF TEST : {((len(result_pass_list) + len(result_fail_list)) / tc_count) * 100}%\n')
f.write(f'PASS RATE : {(len(result_pass_list) / tc_count) * 100}%\n')
f.close()