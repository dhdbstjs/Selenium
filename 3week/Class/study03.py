import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.cgv.co.kr')
driver.implicitly_wait(10)

# 원하는 속성 부분 너무 긴 경우 테스트 할 페이지 접속해서 F12 눌러서 인스펙터 누르고 해당 부분 더블클릭, 컨트롤 C, V

'''find_element() 기본 문법
By : ~으로 찾겠다
By. 뒤에 나오는것이 By 지정자(속성) ,뒤에 나오는것이 그 속성에 대한 속성값
'''


#1 driver.find_element(By.CLASS_NAME, "MyView-module_link_login___HpHMW").click()

#2 driver.find_element(By.ID, 'account').click()
# 로그인페이지로 이동

#3 driver.find_element(By.XPATH, '//*[@id="btn_allView_Movie"]').click()
# 복사할 속성값 지정 후 복사전에 우클릭하면 Copy XPATH 기능이 있다! 그 외에 다른거 지정복사도 가능

#4 driver.find_element(By.CSS_SELECTOR, '#btn_allView_Movie').click()


# time.sleep(3)


''' 실무 팁: 어떤 속성을 이용해야 하나?
가장 덜 바뀌는 속성! 근데 이건 맡은 프로젝트, 부분 별로 다 다르기 떄문에 그 상황에 맞춰서 찾아내야한다 즉, 정답이 없음
사전에 개발자와 협의가 되지 않으면 삽질해야댐
하다 보면서 이 값이 바뀌지 않는구나를 알고 그걸로 지정해서 해야함

자동화 테스트 코드는 왜 항상 사용되지 못할까?
-> 개발 할 때마다 속성값이 계속 바뀌기때문에
-> 유지 보수가 필요하다

자동화 테스트를 하기위해서는 바뀌지 않는 속성 값이 필요함! -> 이 부분은 개발자와 협의해야한다 근데 사실상 너무 많아서 불가능함

ID : 유니크하고 잘 바뀌지 않는 값! 하지만 요소가 너무 많다보니 이 모든것에 ID 불여줄 수 없는 경우가 있어서 잘 정의되지 않는다는 약점이있음
-> 보통 이걸로 지정하고 하긴 함
'''

elem = driver.find_element(By.CSS_SELECTOR, '#btn_allView_Movie')

print(elem.get_attribute('id'))
print(elem.text) # -> 전체보기 라는 텍스트를 뽑아옴
print(elem.location) # -> 로케이션은 딕셔너리 자료형으로 x,y 위치를 반환해준다!

elem = driver.find_element(By.CSS_SELECTOR, "#cgvwrap > div.header > div.header_content > div > h1 > a > img")

elem.screenshot('./cgv_logo.png')
#-> 셀렉터로 찾은 요소 이미지를 스크린샷하고 이 폴더 내에(./) cgv_logo.png 라는 이름으로 저장

# id 의 요소값을 읽어오는데에도 엘리먼트 속성을 사용할 수 있다!
# 이런걸 어디서 사용하나? 페이지 이동시켜주는 링크 태그를 확인 할 때 (a(href), img(src) 등)
# src 변수에 href 속성이 들어가있다거나, 아니면 아예 다른 링크가 걸려있다거나 등

# 자동화 코드를 돌릴 떄 pass는 상관없지만 fail이 떴을 떄 왜 fail이 떴는지 이유를 출력하는게 중요하다!

# 변수명 잘 짓기! elem이라고 지으면 너무 광범위함

