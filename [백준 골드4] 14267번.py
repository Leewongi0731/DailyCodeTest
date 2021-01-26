# 14267번: 회사 문화 1
n, m = list(map(int, input().split()))
parents = [0] + list(map(int, input().split()))
result = [0 for i in range(n+1)]

for _ in range(m):
    i, j = list(map(int, input().split()))
    result[i] += j

for i in range(2, n+1):
    result[i] += result[ parents[i] ]

print( ' '.join(map(str, result[1:])) )