a = int(input())
x = list(map(int, input().split()))
z = 0
for i in range(a):
    y = 0 # 횟수 초기화. 소수면 y 가 몇일까
    print(i, "qwe")
    for l in range(2, x[i]): # 특정 숫자를 2부터 하나씻 나눠본다
        print(l)
        if x[i]%l == 0: #
            y += 1
            print(y, "asd")
        if y == 0:
            z += 1

print(z)