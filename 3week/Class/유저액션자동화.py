import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.cgv.co.kr')
driver.implicitly_wait(10)

# 스크롤
driver.execute_script("window.scrollTo(0, 100);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
time.sleep(2)

elem = driver.find_element(By.CSS_SELECTOR, '#header_keyword')
# driver.find_element(By.CSS_SELECTOR, '#header_keyword').click 이라고 써도 똑같은 결과가 나옴 얘는 객체를 코드내에서 한번만 인식할 때
# 위 코드처럼 나눠서 쓰는 경우는 여러번 동일한 객체에 명령 전달할떄 즉, elem에 여러번 접근 하려고하면 변수 지정해서 따로 써주는게 좋다

elem.click()  # -> 검색창을 클릭해 커서를 띄움
elem.send_keys("토이스토리")
elem.clear() # 객체에 입력했던 값들을 다 지워줌
elem.send_keys("도라에몽")

driver.find_element(By.CSS_SELECTOR, "#btn_header_search").click() #-> 검색 버튼 눌러서 결과 보기


time.sleep(3)

'''
1. find_element 대상을 찾고
2. 상태를 체크하고
3. 흐름을 제어하고
4. 액션을 전달한다
'''