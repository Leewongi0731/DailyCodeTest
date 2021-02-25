# 9465번: 스티커
T = int(input())
for _ in range(T):
    N = int(input())
    datas = [ list(map(int, input().split())) for i in range(2) ]
    
    dp = [ [None, None, None] for i in range(N) ] # N / [위/아래/선택X]
    dp[-1][0], dp[-1][1], dp[-1][2]  = datas[0][-1], datas[1][-1], 0
    
    for n in range(N-2, -1, -1):
        dp[n][0] = max( dp[n+1][1], dp[n+1][2] ) + datas[0][n]
        dp[n][1] = max( dp[n+1][0], dp[n+1][2] ) + datas[1][n]
        dp[n][2] = max( dp[n+1][0], dp[n+1][1], dp[n+1][2] )
        
    result = max( dp[0][0], dp[0][1], dp[0][2] )
    
    print( result )