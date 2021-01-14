# 14501번: 퇴사
N = int(input())
dp = [ [0 for i in range(N+2)] for j in range(N+1) ]
tpData = [ list(map(int, input().split())) for i in range(N) ]

i = 0
for t, p in tpData:
    i += 1
    end = i + t # 해당일 수행하였을때 마무리되는 날
    if end >= N+2: # 수행하지 못하는 경우는 이전날의 최대값으로 set
        dp[i] = dp[i-1]
        continue
    
    for j in range(1, end):
        dp[ i ][ j ] = max( [dp[i-1][j], dp[i][j-1]] )
        
    dp[i][end] = max( [dp[i][i]+p, dp[i-1][end], dp[i][end-1] ] )
    
    for j in range(end+1, N+2):
        dp[ i ][ j ] = max( [dp[i-1][j], dp[i][j-1]] )
        
print(dp[-1][-1])