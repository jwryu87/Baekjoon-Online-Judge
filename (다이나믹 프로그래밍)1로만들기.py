#### 실패 . 나중에 다시 도전


import sys

# def f_3(n):
#     if n % 3 == 0:
#         n = int(n / 3)
#     return n
#
# def f_2(n):
#     if n % 2 == 0:
#         n = int(n / 2)
#     return n
#
# def f_1(n):
#     n = int(n - 1)
#     return n

def f_3(n):
    print("f_3")
    if n % 3 == 0:
        n = int(n / 3)
    print(n)
    f_2(n)

def f_2(n):
    print("f_2")
    if n % 2 == 0:
        n = int(n / 2)
    print(n)
    f_1(n)

def f_1(n):
    print("f_1")
    n = int(n - 1)
    if n == 1:
        print(n)
        sys.exit(1)
    print(n)
    f_3(n)


if __name__ == "__main__":
    n = 10
    i = 1
    # n = int(input())
    f_3(n)
