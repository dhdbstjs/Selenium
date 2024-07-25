# for문 활용 1~10까지 합 구하기

result = 0

for i in range(1, 11, 1):
    result += i

print(result)



# for문 a = [1, 2, 3, 4, 5] 역순 출력

a = [1, 2, 3, 4, 5]

for i in range(4, -1, -1):
    print(a[i])