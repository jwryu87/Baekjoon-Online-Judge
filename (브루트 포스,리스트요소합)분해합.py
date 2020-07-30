import sys
N = int(input())
z = []
if N < 10:
    print(0)
    sys.exit()
for i in range(1, N):
    z.append(i)
    for j in str(i):
        z.append(int(j))
    if sum(z) == N:
        print(i)
        break
    if i == N-1:
        print(0)
        break
    z.clear()