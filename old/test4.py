# arr_count = int(input().strip())
# arr = []
# for _ in range(arr_count):
#     arr_item = int(input().strip())
#     arr.append(arr_item)

arr_count = 5
arr = [10, 8, 7, 6, 5]
value = []

for i in range(arr_count):
    if i >= 1:
        # print("i:", i)
        # print("arr[i]:", arr[i])
        print("arr[:i]", arr[:i])
        for k in range(i):
            # print("k:", k)
            if arr[:i][k] <= arr[i]:
                value.append(arr[i] - arr[:i][k])

if not value:
    print(-1)
else:
    print(max(value))

