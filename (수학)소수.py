import sys

def minor(M, N):
    if N < 2:
        pass
    else:
        for i in range(M, N+1):
            y = 0
            for l in range(2, i):
                if i%l == 0:
                    y += 1
            if y == 0:
                z.append(i)

M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
z = []
minor(M, N)
if not z:
    print(-1)
else:
    if 1 in z:
        z.remove(1)
    print(sum(z))
    print(min(z))