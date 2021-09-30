import sys
import numpy as np
from collections import Counter

N = int(sys.stdin.readline())
z = []
for i in range(N):
    z.append(int(sys.stdin.readline()))
z.sort()

f = np.array(z)

# (1) 산술평균
print(int(round(np.mean(f))))
# (2) 중앙값
print(int(np.median(f)))
# (3) 최빈값
cnt = Counter(f)
if N == 1:
    print(f[0])
else:
    c = cnt.most_common(2)
    if c[0][1] == c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])

# (4) 범위
print(max(f)-min(f))