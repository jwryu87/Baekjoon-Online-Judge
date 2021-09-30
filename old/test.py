import string

# 입력문자
s = 'VGXGPUAMKX'
s_list = list(s)
s_list_cnt = len(s_list)

# 알파벳
x  = list(string.ascii_uppercase)
x1 = list(string.ascii_uppercase)
x2 = x1[::-1]
x1 = x1*1000000
x2 = x2*1000000

# value
value = 0

for i in range(s_list_cnt):
    print(s_list[i])
    print(x1.index(s_list[i]))
    print(x2.index(s_list[i]))
    print("value", min(x1.index(s_list[i]), x2.index(s_list[i])))
    value += min(x1.index(s_list[i]), x2.index(s_list[i]))

    print(x1)
    print(x2)

    x1 = x1[x1.index(s_list[i]):]
    x2 = x2[x2.index(s_list[i]):]

    # print(x1)
    # print(x2)

if s_list[0] == 'Z':
    print(value+1)
else:
    print(value)
