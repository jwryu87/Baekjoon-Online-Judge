# coding=utf-8
#

import itertools

q, w = map(int, input().split())
z = list(map(int, input().split()))
c = itertools.combinations(z, 3)
z = []
f = []
for i in c:
    z.append(sum(i))
for i in range(len(z)):
    f.append(abs(w - z[i]))
print(z[f.index(min(f))])

