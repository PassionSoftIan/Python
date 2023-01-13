# 4. 이걸 1000번 반복한다.
    # 1. 로또 번호 6개를 추첨 받는다.
    # 2. 내가 추첨 받은 6개의 번호가 1049회차 당첨 번호와 일치 하는지 확인한다.
        # 2-1. 확인하는 방법은 내 번호 6개를 순회하면서 1049회 당첨번호 목록에 해당 숫자가 있는지
            # 1049회 당첨번호 목록에 해당 숫자가 있는지
            # 있다면 적중 횟수 + 1
    # 그래서 적중 횟수가 6개면 1등
    # 5개면 3등
    # 4개면 4등
    # 3개면 5등
    # 2개 이하면 꽝을 출력한다.


import random
import requests

r = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1049').json()

first = 0
second = 0
third = 0
fourth = 0
fifth = 0
fail = 0

C = []
for i in range(1, 7) :
    C.append(r[f'drwtNo{i}'])

for i in range(100) :
    numbers = list(range(1, 46))
    A = []

    x = 0

    # while x < 6 :

        # B = random.choice(numbers)
        # A.append(B)
        # numbers.remove(B)
        # x = x + 1

    for i in range(6):
        B = random.choice(numbers)
        A.append(B)
        numbers.remove(B)

    count = 0
    for i in A:
        if i in C:
            count +=1

    if count == 6:
        # print ('당첨 결과:', '1등')
        first += 1
    # elif count == 6: and r['bnusNo'] in A
        # print ('당첨 결과', '2등')
        # second +- 1
    elif count == 5:
        # print ('당첨 결과:', '3등')
        third += 1

    elif count == 4:
        # print ('당첨 결과:', '4등')
        fourth += 1

    elif count == 3:
        # print ('당첨 결과:', '5등')
        fifth += 1

    elif count <= 2:
        # print ('당첨 결과:', '꽝')
        fail += 1


    #print(A)
    #print(C)
    #print(count)
print(f'1등:{first}', f'3등:{third}', f'4등:{fourth}', f'5등:{fifth}', f'꽝:{fail}')
