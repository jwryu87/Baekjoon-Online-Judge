import math

N = int(input())
list = list(map(int, input().split()))
a = len(list)

for i in range(a):
    if a == i+1:
        break
    c = math.gcd(list[0], list[i+1])
    q = list[0]//c
    w = list[i+1]//c
    print("{}/{}".format(q, w))