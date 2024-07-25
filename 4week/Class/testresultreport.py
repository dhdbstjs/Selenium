import os
if not os.path.exists('test_result'):
    os.makedirs('test_result')

# os는 내장모듈
# is not ~가 아니라면 실행하는 구문
# 위 코드는 test_result라는 폴더가 현재 경로에 없으면 만들어라
# makedirs = make directories

f = open('./test_result.txt','w')
f.write("내용 작성합니다")
# W 모드는 같은 파일일 경우 덮어쓴다!

f = open('./test_result.txt','a')
f.write("\n내용 추가합니다")
# a 모드는 추가한다

f.close()
# 파일을 열어놨다가 다 썼으면 닫아줘야한다! 안그러면 다른 사람이 접근 할 때 오류난다
# 근데 이 파이썬 코드가 닫히면 종료되긴 함