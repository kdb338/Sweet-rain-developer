''' result = 8 / (2 * (2 + 2))
print(int(result))

import math   #import는 필요한 기능을 불러올 때 사용하는 키워드예요. 복잡한 수학 계산, 날짜 처리, 파일 작업 같은 건 별도로 불러와야 해요.

A = 550  # 한식당에서 병원까지
B = 600  # 병원에서 햄버거 가게까지

distance = math.sqrt(A**2 + B**2)  #sqrt는 제곱근을 구하는 함수예요.
print(int(distance))

# 시계를 중고로 팔아서 게임기를 사려고 합니다. 백만 원짜리 시계를 15% 할인한 가격은 얼마일까요?

price = 5000
print(int(price * 0.85))

#'pig'에 따옴표가 둘러져 있는 것을 주의해서 보셔야 합니다. 따옴표가 없으면 pig라는 변수로 착각을 하거든요.
# >>> a + ' ' + b = pig dad

# 용량 = r*t
# 다운로드 속도가 초당 800kB이고 다운로드하는 데 걸린 시간이 110초라고 할 때, 다운로드한 파일의 크기는 몇 MB일까요? 단, 1MB = 1000kB로 계산합니다.

용량 = 800*110/1000

print(int(용량))

#리스트는 말 그대로 여러 개의 자료를 묶은 것입니다. 위에서 보신 것처럼 대괄호([ ])랑 콤마(,)를 써서 표현하면 됩니다.

#int는 정수 (integer) 를 뜻해. 소수점 없는 숫자!

num = 1
while num <= 100:
      print(num)
      num = num + 1

# num = num + 1 대신 num += 1로 써도 똑같은 일을 한답니다.
# while 문 마지막에 콜론(:)이 꼭 들어가야하니 빼먹지 마시고요.

num = int(input())

i = 0
while i < num:
    print('', num)
    i += 1

# 아래쪽에 있는 터미널(Terminal) 창에서 사용자가 입력할 수 있어. input() 함수가 실행되면, 이 터미널 창에 커서가 깜빡이면서 "입력 대기" 상태가 돼. 여기에 직접 값을 타이핑하고 Enter 치면 돼!

#정수를 한 개 입력받아, 1부터 입력받은 수까지 각각에 대해 제곱을 구해 프린트하는 프로그램을 작성해 보세요. 단, while 문을 사용하세요.

num = int(input())

i = 1

while i <= num:
    print(i, i * i)
    i = i + 1                            '''


height = 100 # 높이
bounce = 3 / 5

i = 1

while i <= 10:
    height = height * bounce
    print(i, round(height, 4))
    i = i + 1

# 지금 배우는 것과 같은 하찮은 것들이 모여서 엄청난 프로그램도 만들어 내는 것이지요.

