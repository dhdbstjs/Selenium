age = input("나이를 입력해주세요: ")

if int(age) >= 20:  # input으로 입력받은것은 str이기때문에 형변환 해줘야한다
    print("성인")
elif int(age) < 20:
    print("미성년자")






# 길이가 1인 리스트에 1~10 까지 할당하고, 인덱스를 입력받으면 해당 요소가 홀수인지 짝수인지 출력하기

alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

inputindex = int(input("인덱스를 입력하세요: "))   # 형변환

if alist[inputindex] % 2 == 0:   # 형변환 하지 않고 가능 []에 들어가는것은 정수형(인덱스이니까)
    print("짝수")
elif alist[inputindex] % 2 != 0:
    print("홀수")