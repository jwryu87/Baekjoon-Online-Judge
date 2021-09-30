N = str(input())
z = list(N)
# 정렬
z.sort(reverse=True)
# 리스트의 형식 변환
f = list(map(str, z))
# 리스트 배열을 문자열로
a = ''.join(f)
print(int(a))