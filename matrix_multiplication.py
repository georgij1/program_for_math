# Умножение матриц

a = [[1, 1, 0],
     [1, 0, 2]]

b = [[1, 0, 2, 1],
     [2, 1, 2, 0],
     [1, 1, 0, 3]]

m = len(a)  # a: m × n
n = len(b)  # b: n × k
k = len(b[0])

c = [[None for __ in range(k)] for __ in range(m)]  # c: m × k

for i in range(m):
    for j in range(k):
        c[i][j] = sum(a[i][kk] * b[kk][j] for kk in range(n))

print(c)
