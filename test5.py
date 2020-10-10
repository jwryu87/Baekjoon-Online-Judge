import numpy as np

arr_count = 5
arr = [5, 3, 5, 7, 4]

value = []

for i in range(arr_count):
    arr2 = []
    if i >= 1:
        # print("i:", i)
        # print("arr[i]:", arr[i])
        print("arr************", arr[:i])
        for l in range(i):
            arr2.append(arr[i])
        print("arr2-------------:", arr2)
        x = np.array(arr[:i])
        y = np.array(arr2)
        print(x)
        print(y)
        z = y-x
        print(z.tolist())
        # value.append(z)
# print(value)