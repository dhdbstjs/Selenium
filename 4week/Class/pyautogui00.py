'''
셀레니움은 대상 자체를 인식
파이오토는 대상 자체 인식은 못하고 단순히 좌표 기반으로 인식! 그렇기 떄문에 창을 띄울 때 사이즈 조정이 필요하다(사용자마다 화면 픽셀이 다르니까)
파이오토가 간단하지만 셀레니움의 기능이 더 강력함 -> 근데 왜 파이오토를 쓰라고 하는가?

pip install pyautogui
'''

# 모듈은 도구의 모음. 즉, 파일에 작성되어있는 코드들의 모음이기때문에 파일이다! -> 연습할 떄 파일 이름을 모듈명과 같은 이름을 사용하면 오류남

import pyautogui

mouse_position = pyautogui.position()
print(mouse_position)