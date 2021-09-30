from itertools import permutations # permutations 이 순열

a, b = map(int, input().split())
z = []
for i in range(a):
    z.append(i+1)

P = permutations(z, b) # permutations ( 리스트, 조합횟수 )

# 출력 시 아래와 같이 출력한다
for i in P:
    print(' '.join(map(str, i)))  # tuple -> str
