coin, value = map(int, input().split())
list = []
for i in range(coin):
    list.append(int(input()))
    list.sort(reverse=True)
result = 0
for i in range(coin):
    if value >= list[i]:
        coin_cnt = value // list[i]
        value -= coin_cnt * list[i]
        result += coin_cnt

print(result)