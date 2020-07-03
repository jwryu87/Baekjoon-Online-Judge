try:
    q = int(input())
    if q < 5 and q % 3 != 0:
        print(-1)
    elif q == 5:
        print(1)
    elif q == 0:
        print(-1)
    elif q % 5 % 3 == 0:
        value_1 = q // 5
        value_2 = q % 5 // 3
        print(value_1 + value_2)
    else:
        for i in range(q // 5 + 1):
            if (q - (5 * i)) % 3 == 0:
                value_1 = i
                value_2 = (q - (5 * i)) // 3
                a = value_1 + value_2
                b = value_1
                c = value_2
        print(a)
except:
    print(-1)