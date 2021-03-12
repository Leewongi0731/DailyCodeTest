# 17070번: 파이프 옮기기 1
from collections import deque

N = int(input())
table = [ list(map(int, input().split())) for i in range(N) ]

dp = [ [[ 0 for i in range(3) ] for i in range(N)] for i in range(N) ] # i, j, dic -> count
dp[0][1][0] = 1 # 시작 (0,0), (0,1)에서 수평 방향

for i in range(N):
    for j in range(N):
        if table[i][j]==1: continue
        
        if 0<=j-1 and table[i][j-1]!=1: # 가로 이동해서 오는경우
            dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][2]
        
        if 0<=i-1 and table[i-1][j]!=1: # 세로 이동해서 오는 경우
            dp[i][j][1] += dp[i-1][j][1] + dp[i-1][j][2]
        
        if 0<=i-1 and 0<=j-1 and table[i-1][j-1]!=1 and table[i-1][j]!=1 and table[i][j-1]!=1: # 현재 기준에서 좌측 대각선에서 오는경우
            dp[i][j][2] += dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
            
        
print( sum(dp[N-1][N-1]) )