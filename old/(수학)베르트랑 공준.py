# coding=utf-8
#
import sys

# n보다 크고 2n 보다 작은 소스는 적어도 하나 존재한다
# n이 주어졌을 때 n보다 크고, 2n 보다 작거나 같은 소수의 개수를 구하라

def ver(n):
    n2 = 2* n
    x = []
    for i in range(n+1, n2+1):
        x.append(i)
    a = n2-n
    z = 0
    for i in range(a):
        y = 0 # 횟수 초기화. 소수면 y 가 몇일까
        for l in range(2, x[i]): # 특정 숫자를 2부터 하나씻 나눠본다
            # print(x[i], l)
            if x[i]%l == 0: # 하나라도 나눠지는게 없다면 소수
                y += 1
                # print(y, "asd")
        if y == 0:
            z += 1
    if z > 0:
        return print(z)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    ver(n)


# 문제점: 속도를 더 빠르게 해야한다.