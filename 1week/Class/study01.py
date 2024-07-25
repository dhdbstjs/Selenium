# 변수에서의 =은 같다는 뜻이 아니고 할당한다는 의미
# a에 할당한 데이터가 변함으로써 다른 값이 나옴

a = 5
print(a)

a = 8
print(a)




# 변수끼리의 연산
# f-string formatting: 문자열을 생성하는 방식 중 하나
# f' {데이터}' 중괄호 밖에 있는 데이터는 문자열

a = 5
b = 3

print(f'a + b = {a+b}')

a = 8
b = 3

print(f'a + b = {a+b}')




a = 6 - 2
print(a)

a = 2; b = 6
print(a - b)



# a = 6
# b = 0
# print(a / b)
#ZeroDivisionError: division by zero



a = 6 % 2
print(a)

a = 7; b = 2
print(a % b)




a = "오늘 저녁은 "
b = "맛있는 "
c = "한식!"

print(f'{a}{b}{c}')
print(a + b + c)

# string 할당할 때 정석은 쌍따옴표를 쓴다 (파이썬 권장 방식)
# character은 홑따옴표




# 자동화 코드를 만들 때 시간관련된 코드를 자주 쓰게될것이다
# 개발자에게 이 시각에 실행된게 오류가 떴다고 알려줄 수 있기 때문




# 형변환 (일시적 변환)
a = '5'
b = 3
print(int(a) + b)
print(a + str(b))




# 리스트
a = [1, 2, 3, 4, 5]
print(a)


print(a[0])
print(a[3])




# 자주쓴다 append() 메소드
# 리스트의 뒤쪽으로 추가가 된다

# 함수와 메소드의 차이? https://velog.io/@yejin20/Python-%ED%95%A8%EC%88%98%EC%99%80-%EB%A9%94%EC%86%8C%EB%93%9C%EC%9D%98-%EC%B0%A8%EC%9D%B4%EC%A0%90

a = []
a.append(1)
a.append(2)
print(a)


# insert는 인덱스로 위치를 지정하고 그 위치에 추가함
# insert(1, 6) -> 인덱스 [1]에 6을 추가하라

# 인덱스의 위치를 지정하고 새로운 값 할당하면 데이터 바뀜

# del a[0] 처럼 인덱스 번호를 지정해 해당 요소 삭제 가능

a = [1, 2, 3, 4, 5]
print(len(a))

# 반복문 쓸 때 len을 가장 많이 쓴다
# ex. 3번 반복인데 리스트 요소 2개밖에 없으면 오류남


# api 서버 <-> 클라이언트 주로 json 파일 형태로 주고받는다
# 딕셔너리와 json 자료형 구조가 같아서 json 파일을 불러온것을 파이썬을 통해 바로 딕셔너리형으로 만들 수 있다
# api 테스트는 필수로 하게된다 자동화테스트에서
# a = {'fruit' : 'apple'} 이런식의 형태로 되어있음
# 딕셔너리에 접근할 때는 인덱스 값이 아닌 키값으로 밸류에 접근한다! 리스트와 비슷해보이지만 다름 key : value

a = {}   #딕셔너리 선언
a['fruit'] = 'apple'   #이런식으로 키, 밸류값 할당




# if 중첩문은 지양하는 분위기??
a = 20

if a > 10:
    print("a는 10보다 큽니다")

if a < 10:
    print("a는 10보다 작습니다")




# 입력 명령어 input!
# 입력받은 값은 문자열이다

a = input("정수를 입력해주세요")

if int(a) % 2 == 0:
    print("a는 짝수입니다")

if int(a) % 2 != 0:
    print("a는 홀수입니다")



a = input("정수 입력하세요")

if int(a) % 2 == 0:
    print("a는 짝수입니다")
elif int(a) % 2 != 0:
    print("a는 홀수입니다")


# elif를 사용하는 이유?
# 같은 데이터의 조건을 비교할 때 if가 많을수록 비효율적임
# elif를 사용하면 해당이 되는것에만 걸렸다가 결과를 내지만 if만 사용하게되면 if 만날 때마다 비교를 하기 때문에




cnt = 0

while(cnt < 10):    # True일때 무한반복
    print(f'{cnt + 1}번째 반복')
    cnt += 1


# flag를 이용해서 반복을 제어하는 경우도 있다
# 근데 이럴 경우 변수가 괜히 하나 더 늘어나서 잘 사용하지 않지만 
# 조건이나 상황이 변경되었을 때 사용한다
# 1~2시 반복하는 코드가 있는데 0 일때만 반복을하는 조건이라고 하자. 시간을 계속 계산하다가 그 시간이 넘어가면 flag를 1로 바꿔서 종료하는 식으로 사용한다


for a in range(0, 5, 1):
    print(a)


for a in range(5, 0, -1):   # 끝나는 값은 입력된 값 까지가 아니고 그 전 값까지임! 헷갈리지 말자!
     print(a)


# 리스트 항목 출력할 때 반복문을 가장 많이 사용한다

a = [1, 2, 3, 4, 5]

for cnt in range(len(a)):  # 0~5
    print(a[cnt])   # cnt라는 변수를 인덱스값으로



# break, continue 실무에서 실제로 많이 사용되지 않음