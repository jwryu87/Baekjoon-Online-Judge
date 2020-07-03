# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.
#
# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
#
# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# Mississipi
# ?
#
# zza
# z

def asd (f, u):
    zx = []
    for k, v in f.items():  # mydict에 아이템을 하나씩 접근해서, key, value를 각각 name, age에 저장
        if v == u:
            zx.append(k)
    if len(zx) > 1:
        print('?')
    else:
        print(zx[0])

# q = 'zza'
q = str(input()) # str 으로 입력받고
q = q.upper() # 모두 대문자로 변환
w = list(q) # str을 각각으로 구분하여 리스트로 저장
r = list(set(w)) # 리스트 distinct
t = len(r) # 고유한거 몇개 있는지
d = {} # 딕셔너리
f = {} # 딕셔너리
for i in range(t):
    # d = {r[i]: w.count(r[i])}
    # d[r[i]] = w.count(r[i])
    d[w.count(r[i])] = r[i] # 각 단어 카운트한거를 딕셔너리로 저장
    f[r[i]] = w.count(r[i])  # 각 단어 카운트한거를 딕셔너리로 저장
u = max(f.values())
# print(f)
asd(f, u)


