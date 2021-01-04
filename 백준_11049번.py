# 11049번: 행렬 곱셈 순서
def getDP( i, j ):
    if i == j:
        return 0
    elif dp[i][j] != 0:
        return dp[i][j]
    
    tmp = []
    for k in range(i, j):
        tmp.append( getDP( i, k ) + getDP(k+1, j) + data[i-1]*data[k]*data[j]  )
    dp[ i ][ j ] = min(tmp)
    return dp[i][j]
#####################################
N = int(input())
data = [0 for i in range(N+1)]
dp = [ [0 for i in range(N+1)] for j in range(N+1) ]

for i in range(N):
    r, c = list(map(int, input().split()))
    data[i] = r
    data[i+1] = c
    
print( getDP(1, N) )