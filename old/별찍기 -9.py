# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
# 5
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********
a = int(input())
b = 2 * a
for i in range (b-1, 0, -2):
    # print("*" * i)
    print("{:^{}}".format("*" * i, b))
for i in range (3, b, 2):
    # print("*" * i)
    print("{:^{}}".format("*" * i, b-1))