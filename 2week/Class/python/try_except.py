# 예외처리 try-except 구문 사용
# 에러는 발생할 수 있다. 근데 이때 예외처리가 되어있지 않으면 코드가 죽는다! 이렇게 되면 안되니까 예외처리는 필수
# except 에러 이름 as e
# 어떤 에러가 발생할 지 모를 때 Exception으로 포괄적으로 쓰는거! 특정 에러가 아니라 모든 에러가 대상일 때
# as e 는 Exception을 또 쓸건데 앞으로 Exception을 앞으로 e 로 줄여서 쓰겠다는 의미임! e = Exception
# 이 코드 실행하면 {e}에 division by zero 로 뜬다 에러구문을 실행


# <<<< 자주 발생하는 예외 >>>>

# 0으로 나눌 떄
try:
    if 5/0 >= 1:
        print("1보다 크다")
    else:
        print("1보다 작다")
    print("계산 종료")
except Exception as e:
    print(f'나눗셈 에러 발생!! >>> {e}')

print("에러 발생 이후 코드")



# 리스트 크기보다 더 큰 인덱스로 요소에 접근할때
alist = [1, 2, 3]

try:
    print(alist[4])
except Exception as e:
    print(f'리스트 크기보다 큰 값을 입력했습니다 >>> {e}')



# 숫자와 문자열을 합칠 때
num1 = 1
string1 = '2'

try:
    print(num1 + string1)
except Exception as e:
    print(f'숫자와 문자열은 더할 수 없습니다 >>> {e}')