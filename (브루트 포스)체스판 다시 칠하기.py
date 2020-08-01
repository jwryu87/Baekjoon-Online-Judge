# 제시된 것
N, M = map(int, input().split())
N = 10
M = 13
z = []
b = []
for i in range(N):
    z.append(list(input()))
print(z)

# 올바른 것
for i in range(N):
    a = []
    if z[i][0] == 'W':
        a = list(str('WB' * 25))
        b.append(a[:M])
    elif z[i][0] == 'B':
        a = list(str('BW' * 25))
        b.append(a[:M])
print(b)

# z, b 비교
c = 0
for i in range(N):
    for j in range(M):
        if z[i][j] == b[i][j]:
            pass
        else:
            c += 1
print(c)

# 문제자체가 이해하기 힘들어서 여기까지함
