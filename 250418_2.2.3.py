'''
a = 1234 * 4
b = 13456 / 2

if a > b:                     # 만약 a가 b보다 크면
    print('a')                # 'a'를 출력한다.
else:                         # 그렇지 않으면
    print('b')                # 'b'를 출력한다.


c = 15 * 5
d = 15 + 15 + 15 + 15 + 15

if c > d:
     print('c is greater than d')
elif c == d:
     print('c is equal to d')
elif c < d:
     print('c is less than d')
else:
     print('I don\'t know')        #\는 이스케이프 문자 (escape character) 라고 해! 파이썬에서 문자열은 ' 또는 "로 감싸서 만들지? 근데 문자열 안에 '가 들어가면, 파이썬이 그걸 문자열의 끝으로 착각할 수도 있어.
 
# 결과: c is equal to d

a = 48
b = 4
if a % b == 0:
    print(f'{a}는 {b}로 나누어 떨어집니다.')
elif a % b != 0:
    print(f'{a}는 {b}로 나누어 떨어지지 않습니다.')

# 48는 4로 나누어 떨어집니다. elif a % b != 0: 대신 else:라고 해도 결과는 같겠죠?

#일관된 들여쓰기 사용: 스페이스바 4칸 또는 탭 키 하나를 선택해서 코드 전체에서 일관되게 사용하시는 것이 중요합니다. 섞어서 사용하면 오류가 발생하기 쉽습니다.

max = 10

while True:   #"이 조건이 **참(True)**인 동안 계속 반복해!" 라는 뜻이야. 어떤 **블록(묶음)**을 만들 때, 꼭 :을 붙여서 알려줘야 해.
    num = int(input())
    if num > max:
        print(num, 'is too big!')
        break


# input()을 사용해 사용자로부터 입력받은 숫자를 한글로 출력하는 프로그램을 작성하세요. 단, 사용자는 1 이상 3 이하의 정수 중 하나를 입력한다고 가정합니다.

num = int(input())

if num == 1:
    print('일')
elif num == 2:
    print('이')
elif num == 3:
    print('삼')



y = int(input('What year were you born? '))

gen = None

if y <= 1924:
    gen = 'the Greatest Generation'
elif y <= 1945:
    gen = 'the Silent Generation'
elif y <= 1964:
    gen = 'a baby boomer'
elif y <= 1980:
    gen = 'a Gen X'
elif y <= 1996:
    gen = 'a millennial'
else:
    gen = 'a Gen Z'

print(f"You're {gen}.")

num = int(input())
result = str(num)
            
if num >= 1000:
     result = str(num // 1000) + 'k'
elif num >= 0:
      pass
     
print(result)

# str 말이죠! 문자열(string) 자료형을 나타내는 키워드예요.

# 1~100자리 숫자를 생략하려고 정수의 나눗셈(//)을 이용했습니다.

'''

num = int(input())
result = str(num)
            
if num >= 100000:
     result = str(num // 100000) + 'M'
elif num >= 1000:
     result = str(num // 1000) + 'k'
elif num >= 0:
      pass
     
print(result)