N = int(input())
def pf(N):
    for i in range(2, N + 1):
        if N % i == 0: # 값을 나누어서 딱떨어지면
            print(i)
            N = N // i # 나누어진 값으로 다시 시작한다.
            if N == 1:
                quit()
            pf(N)

pf(N)