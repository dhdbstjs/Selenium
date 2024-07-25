# requests 모듈
# pip install requests
# 리퀘스트는 서버에 요청보내고 서버에서 응답 받아오는거라서 브라우저를 띄우지 않는다!
# 셀레니움이랑 같이 많이 사용되는 모듈!
# 셀레니움은 엘리먼트를 인식하기때문에 그 자체의 부재를 인식 가능한데 파이오토는 무작정 띄워서 작동하기때문에 파이오토만 사용하면 신뢰도가 떨어진다

import requests

response = requests.get("https://google.co.kr")
print(response.text)
# 출력된 메세지 맨 처음에 <!doctype html>이라고 뜬다 html 파일이라는것을 알 수 있음
print(response.status_code)

'''
status_code 출력했을 때 결과가
200번대 코드는 상태 좋음!
300번대
401 커미션 에러 -> 권한 없는곳에 접근하려했다
404 -> page not found
400 클라이언트 웹프론트 문제
500 서버에 문제
'''

# 리퀘스트로 먼저 상태 확인한 후에 문제가 있으면 UI 자동화 스텝인 셀레니움을 실행하지 않는 등 유연하게 모듈들을 함께 사용할 수 있다