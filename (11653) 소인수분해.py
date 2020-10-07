import math

# N = int(input())
N = 6
z = []

def pf(N):
    for i in range(2, N + 1):

        print("시작", N, i)
        if N % i == 0: # 값을 나누어서 딱떨어지면
            print("넘어옴", N, i)
            print(i)
            N = N // i # 나누어진 값으로 다시 시작한다.
            print(N)
            if N == 1:
                quit()
            print("종료", N, i)
            pf(N)

pf(N)

# 값을 숫자 하나씩 나눈다
# 딱떨어지면
# 그 숫자를 저장하고
# 나머지로 또 나눈다다