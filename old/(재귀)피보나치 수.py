# coding=utf-8
#

def fib(N):
    if N == 0:
        return
    a = z[0]
    b = z[1]
    c = a+b
    x.append(c)
    z.clear()
    z.append(b)
    z.append(c)
    # print(x)
    N -= 1
    fib(N)

if __name__ == "__main__":
    N = int(input())
    z = [0, 1]
    x = [0, 1]
    fib(N)
    print(x[N])


    