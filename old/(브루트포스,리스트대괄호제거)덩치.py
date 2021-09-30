N = int(input())
x = []
y = []
e = []
for i in range(N):
    a, b= map(int, input().split())
    x.append(a)
    y.append(b)

for j in range(N):
    r = 0
    for k in range(N):
        if x[j] < x[k] and y[j] < y[k]:
            r += 1
    e.append(r+1)
print(' '.join(map(str, e)))

