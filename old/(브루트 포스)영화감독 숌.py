import re

N = int(input())
a = 0
z = 0
while True:
    z += 1
    if bool(re.findall(r'666', str(z))):
        a += 1
        if N == a:
            print(z)
            break

