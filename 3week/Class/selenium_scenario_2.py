import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.cgv.co.kr')
driver.implicitly_wait(10)

cgv_url = driver.current_url
if cgv_url == 'https://www.cgv.co.kr/':
    print('cgv 접속 성공')
else:
    print(cgv_url)
    print('cgv 접속 실패')

elem = driver.find_element(By.CSS_SELECTOR, '#header_keyword')
elem.click()
elem.send_keys('28tu9w8g')

driver.find_element(By.CSS_SELECTOR, '#btn_header_search').click()
driver.implicitly_wait(10)

elem = driver.find_element(By.CSS_SELECTOR, '#search_result')
origin_text = '\'28tu9w8g\' 寃��됯껐怨쇨� �놁뒿�덈떎.'
if origin_text == elem.text:
    print('鍮꾩쑀�⑦븳 �곹솕 �대쫫 寃��� �깃났.')
else:
    print('鍮꾩쑀�⑦븳 �곹솕 �대쫫 寃��� �ㅽ뙣.')

driver.find_element(By.CSS_SELECTOR, '#cgvwrap > div.header > div.header_content > div > h1 > a > img').click()
driver.implicitly_wait(10)
elem = driver.find_element(By.CSS_SELECTOR, '#contaniner > div.noticeClient_wrap > div > div.noticeClient_container > div.qr_wrap > div > img')
if elem.is_displayed():
    print('�덊럹�댁� �대룞 �깃났.')
else:
    print('�덊럹�댁� �대룞 �ㅽ뙣.')