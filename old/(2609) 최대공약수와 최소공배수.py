a, b = map(int, input().split())
d = a*b

# while True:
#     if a > b:
#         a = a % b
#         if a == 0:
#             c = b
#             break
#     elif b > a:
#         b = b % a
#         if b == 0:
#             c = a
#             break
#
# print(c)
# print(d//c)

# 위에 걸로 시간초과 떠서 math로 함
import math
c = math.gcd(a, b)
print(c)
print(d//c)