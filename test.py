import bisect
a = [1, 2, 4, 5, 3, 10, 15, 13, 14]
b = 12
print(bisect.bisect(a, b))
print(bisect.bisect_left(a, b))
print(bisect.bisect_right(a, b))