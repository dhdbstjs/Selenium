# 리퀘스트는 좌표 기준이라서 브라우저를 띄워줄 필요가 있다

import pyautogui
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.cgv.co.kr")
driver.implicitly_wait(10)

# mouse_position.exe 실행시키고 나서 좌표 확인하기
pyautogui.moveTo(1249, 452)
pyautogui.click(1249, 452)

pyautogui.click(1055, 458)
pyautogui.typewrite("www")
pyautogui.typewrite("www", interval=0.5)

# 작업관리자 창 ctrl shift del -> 프로세스 -> 마우스포인터 exe 작업 종료

'''
pyautogui.keyDown('ctrl')
pyautogui.press('a')

-> 이런식으로 조합해서 사용할 수 있다! 전체선택
'''

pyautogui.screenshot('C:/Users/USER/Desktop/Selenium_Empty/4week/myscreenshot2.png', region=(0,0, 1920, 1080))