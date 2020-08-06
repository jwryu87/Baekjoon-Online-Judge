import sys
N = int(input())
dic = {}
for i in range(N):
    a, b = map(str, sys.stdin.readline().split())
    dic[b] = a
dic_modify = sorted(dic.items(), key=lambda x: x[1])
for i in range(N):
    dic_list = list(dic_modify[i])
    dic_list.reverse()
    print(' '.join(dic_list))
