#while 문을 이용해 사용자에게 'exit'를 입력받기 전까지 계속 입력받기.

while(True):
    a = input("입력값을 넣으세요! exit를 입력하면 종료합니다.")
    if a == "exit":
        break