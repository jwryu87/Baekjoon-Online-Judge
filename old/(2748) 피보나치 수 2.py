N = int(input())
# 90가지 요소를 가지고 있는 피보니치 수열을 만들고
z = [0, 1]
a = 2
while len(z) <= 90:
    z.append(z[a-1] + z[a-2])
    a += 1
# N번째 피보나치 수열을 뽑는다.
print(z[N])