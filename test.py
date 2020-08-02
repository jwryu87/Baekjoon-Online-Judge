n = 2
cnt = 0
six_n = 666
while True:
    if '666' in str(six_n):
        cnt += 1
    if cnt == n:
        print(six_n)
        break
    six_n += 1

import re

N = int(input())
a = []
# while True:
for i in range(1, 10000):
    z = str(i)
    # print(z)
    if bool(re.findall(r'666', z)):
        a.append(int(z))
print(a)
print(a[N-1])

