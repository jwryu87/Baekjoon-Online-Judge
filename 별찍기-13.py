# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
# 3
# *
# **
# ***
# **
# *
a = int(input())
b = 2 * a
for i in range (1, b):
    print("*" * i)
    if i == a:
        for i in range(a-1, 0, -1):
            print("*" * i)
        break