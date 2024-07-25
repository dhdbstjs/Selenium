#1. Selenium과 Python을 이용해 임의의 페이지 5개에 접근하기.
#2. 접근한 페이지들의 타이틀을 title = [] 리스트에 추가하기.
#3. 접근한 페이지들의 URL을 url = [] 리스트에 추가하기.
#4. title 리스트와 url 리스트를 출력하기.


from selenium import webdriver

driver = webdriver.Chrome()

page_list= ['https://naver.com', 'https://daum.net/', 'https://google.co.kr', 'https://youtube.com', 'https://netflix.com']
title = []
url = []

for i in range (5):
    driver.get(page_list [i])
    title.append(driver.title)
    url.append(driver.current_url)
    i += 1

print(title)
print(url)