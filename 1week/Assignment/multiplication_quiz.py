#1~10 사이의 정수를 입력받아 해당 구구단 단을 출력하기.

gugudan = int(input("구구단을 출력할 1~10 사이의 정수를 입력하세요: "))

for i in range(1, 10, 1):
    print(f'{gugudan} x {i} = {gugudan * i}')
    i += 1