# 1000 70 170
# 11

q, w, e = map(int, input().split())
t = 0
if w >= e:
    print(-1)
else:
    print(q // (e - w) + 1)