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


--> 이렇게 하면 런타임 에러가 나는데
해결하려면 Lambda를 이용해서 정렬해야 한다고 한다...