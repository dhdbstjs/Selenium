import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://comento.kr/?index")
error_log = driver.get_log('browser')
time.sleep(2)
# UI를 불러와서 확인하는 경우에는 딜레이가 있을 수 있다. 코드에 문제가 없는데 자꾸 오류가 뜬다면 time을 활용해 불러오는데 기다려주는 시간을 넣을 것!

# print(error_log)
# 에러메세지들이 출력되는데 [] 리스트 형태로 에러메세지가 출력된다
# 그 안의 요소들은 {} 딕셔너리 형태

print(error_log[0]['level'])
# 인덱스를 선택 여러 딕셔너리 요소중에 key값 level에 대응하는 밸류값을 불러옴 -> 'level': 'WARNING' -> # WARNNG 메세지 출력

# INFO : 정보 / WARNING : 경고 / SEVERE : 심각한 오류