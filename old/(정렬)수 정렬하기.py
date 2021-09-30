N = int(input())
z = []
for i in range(N):
    z.append(int(input()))
z.sort()
for i in range(N):
    print(z[i])