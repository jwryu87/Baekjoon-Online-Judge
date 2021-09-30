N = int(input())
z = []
for i in range(N):
    z.append(str(input()))
# set으로 중복제거
q = set(z)
z = list(q)
z.sort()
# 리스트를 길이순으로 정렬
f = sorted(z, key=len)
# z.sort(z, key=len)
for i in f:
    print(i)
