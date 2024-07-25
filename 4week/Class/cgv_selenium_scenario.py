#내용 유지할것
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

#전체 예외처리
try:
    # 현재 시간 구하기
    now = time.strftime('%Y_%m_%d_%Hh_%Mm')

    result_pass_list = [] # 성공한 TC 담는 리스트
    result_fail_list = [] # 실패한 TC 담는 리스트
    fail_reason_list = [] # 실패한 이유 담는 리스트
    tc_count = 3

    # 테스트 리포트 파일이 저장될 폴더 만들기
    if not os.path.exists('test_result'):
        os.makedirs('test_result')

    # 언제 실행됐는지 알기위해
    f = open(f'./test_result/{now}_Test_report.txt', 'w')

    driver = webdriver.Chrome()
    driver.get('https://www.cgv.co.kr')
    driver.implicitly_wait(10)

    try:
        tc_id = "TC_001"
        cgv_url = driver.current_url
        if cgv_url == 'https://www.cgv.co.kr/':
            print('cgv 접속 성공.')
            result_pass_list.append(tc_id)
        else:
            print(cgv_url)
            print('cgv 접속 실패.')
            result_fail_list.append(tc_id)
            fail_reason_list.append("cgv 접속 실패.")

    except Exception as e:
        print(f"TC_001번 테스트 수행 오류 발생 >>> {e}")

    try:
        tc_id = "TC_002"
        elem = driver.find_element(By.CSS_SELECTOR, '#header_keyword')
        elem.click()
        elem.send_keys('28tu9w8g')

        driver.find_element(By.CSS_SELECTOR, '#btn_header_search').click()
        driver.implicitly_wait(10)

        elem = driver.find_element(By.CSS_SELECTOR, '#search_result')
        origin_text = '\'28tu9w8g\' 검색결과가 없습니다.'
        if origin_text == elem.text:
            print('비유효한 영화 이름 검색 성공.')
            result_pass_list.append(tc_id)
        else:
            print('비유효한 영화 이름 검색 실패.')
            result_fail_list.append(tc_id)
            fail_reason_list.append("비유효한 영화 이름 검색 실패.")

    except Exception as e:
        print(f"TC_002번 테스트 수행 오류 발생 >>> {e}")

    try:
        tc_id = "TC_003"

        driver.find_element(By.CSS_SELECTOR, '#cgvwrap > div.header > div.header_content > div > h1 > a > img').click()
        driver.implicitly_wait(10)
        elem = driver.find_element(By.CSS_SELECTOR, '#contaniner > div.noticeClient_wrap > div > div.noticeClient_container > div.qr_wrap > div > img')
        if elem.is_displayed():
            print('홈페이지 이동 성공.')
            result_pass_list.append(tc_id)
        else:
            print('홈페이지 이동 실패.')
            result_fail_list.append(tc_id)
            fail_reason_list.append("홈페이지 이동 실패.")
    
    except Exception as e:
        print(f"TC_003번 테스트 수행 오류 발생 >>> {e}")

except Exception as e:
    print(f'테스트 실행 실패! >>> {e}')



# 통계 작성
f.write(f"테스트 수행 일자 - {now}")
f.write("\n[RESULT - PASS]\n")

for pass_cnt in range(len(result_pass_list)):
    f.write(f"{result_pass_list[pass_cnt]}\n")

f.write("\n[RESULT - FAIL]\n")

for fail_cnt in range(len(result_fail_list)):
    f.write(f"{result_fail_list[fail_cnt]}\n")
    f.write(f"\t{fail_reason_list[fail_cnt]}\n")

f.write("==========================\n")
f.write(f"PASS TC COUNT : {len(result_pass_list)}\n")
f.write(f"FAIL TC COUNT : {len(result_fail_list)}\n")
f.write(f"COMPLETED TEST COUNT : {len(result_pass_list) + len(result_fail_list)}\n")
# 수행한 TC 개수 / 전체 TC 개수 * 100
f.write(f'PROGRESS OF TEST : {((len(result_pass_list) + len(result_fail_list)) / tc_count) * 100}%\n')
f.write(f'PASS RATE : {(len(result_pass_list) / tc_count) * 100}%\n')
f.close()