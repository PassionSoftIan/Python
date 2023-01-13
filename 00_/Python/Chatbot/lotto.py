import random

# 1 - 45 숫자를 담은 list 생성
# rage(n, m) = n부터 m-1 까지의 숫자를 생성
numbers = list(range(1, 46))

# numbers가 가진 숫자 중에 무작위 값을 하나씩 6번 뽑기
# 리스트가 가지고 있는 값 중에 무작위 값을 뽑는 방법은?

# print(random.choice(numbers))

# while문을 사용하여 뽑아보기.

x = 0

while x < 6 :

    print(random.choice(numbers))
    x = x + 1

