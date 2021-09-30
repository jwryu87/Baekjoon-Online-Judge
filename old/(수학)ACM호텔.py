def loop(h, w, e):
    y = 0
    for i in range(1, w+1):
        # print(i + 100)
        for l in range(1, h+1):
            # print(i + 100 *l)
            y = y + 1
            if y == e:
                print(i + 100 *l)
                break

x = int(input())
for q in range(x):
    h, w, e = map(int, input().split())
    loop(h, w, e)