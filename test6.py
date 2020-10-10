import string

n = 702
C = n // 702 + 1 # 알파벳 숫자
R = n % 702 - 1  # 행 숫자

print(C, R)

# 알파벳
col = list(string.ascii_uppercase)
col_1 = list(string.ascii_uppercase)
col_cnt = len(col)
col_1.extend([i+k for i in col for k in col])
# col_1.extend([i+k+l for i in col for k in col for l in col])
print(col_1[-1])
print(col[R])

print("{0}{1}".format(C, col[R]))