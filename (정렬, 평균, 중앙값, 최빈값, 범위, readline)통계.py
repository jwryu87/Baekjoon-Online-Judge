import sys
import numpy as np
from collections import Counter

N = int(sys.stdin.readline())
z = []
for i in range(N):
    z.append(int(sys.stdin.readline()))
z.sort()
z = np.array(z)
print(int(round(np.mean(z))))
print(int(np.median(z)))
cnt = Counter(z)
if N == 1:
    print(z[0])
else:
    c = cnt.most_common(2)
    if c[0][1] == c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])
print(max(z)-min(z))