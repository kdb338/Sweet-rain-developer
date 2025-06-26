'''
for x in family:        # family의 각 항목 x에 대하여:
    print(x, len(x))    # x와 x의 길이를 출력하라.


list(range(2, 7))
range(2, 7)

num = int(input())

for i in range(num):
    print('', num) #''은 앞에 공백을 넣기 위해


L = input().split()   # split()은 구분자를 안 쓰면 공백(스페이스, 탭, 줄바꿈 포함) 기준으로 자동으로 나눠.
min = int(L[0])
max = int(L[1])
# min, max = map(int, input().split())

temp = int(input())

while temp != -999:   # !=는 **"같지 않다"**를 뜻하는 비교 연산자야.
    if min <= temp <= max:
        print('Nothing to report')
        temp = int(input())
    else:
        print('Alert!')
        break

# while 문도 마찬가지입니다. while 문이 break될 경우에는 else 블록이 실행되지 않습니다.

len(a_list)

def print_list(a):  # 지금부터 print_list 함수를 만들겠다는 뜻
    for i in a:
            print(i)

# def는 파이썬에서 **함수(function)**를 정의할 때 사용하는 키워드야.

# str은 **"string"**의 줄임말이잖아?

# 아주 아주 아주 많은 주소를 만들 수 있는 IPv6로 바꿔 가고 있다고 합니다. IPv6 주소는 2001:0db8:85a3:0000:0000:8a2e:0370:7334처럼 생겼고 2128개의 주소를 만들 수 있습니다.

'''

def multi(m):   # 함수명으로 쓴 거임
    for n in range(1, 10):
        print(f'{m} * {n} = {m*n:2d}')   # 자리수를 맞추려고 f-문자열의 세 번째 중괄호에 2d를 지정했습니다.

if __name__ == '__main__':
    for i in range(2, 10):
        multi(i)
        print()

# 파이썬의 f-문자열은 문자열 안에 변수나 표현식을 아주 간단하고 깔끔하게 넣을 수 있는 문법이야.

3.1.2