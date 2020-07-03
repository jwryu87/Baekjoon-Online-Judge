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
                print(i)

M, N = map(int, sys.stdin.readline().rstrip().split())
minor(M, N)