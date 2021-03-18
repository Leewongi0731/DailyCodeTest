# 11048번: 이동하기
N, M = list(map(int, input().split()))
table = [ list(map(int, input().split())) for i in range(N) ]
dp = [ [0 for i in range(M)] for i in range(N) ]
dp[0][0] = table[0][0]

mx, my = [1,0,1], [0,1,1]
for i in range(N):
    for j in range(M):
        for z in range(3):
            ii,jj = i+mx[z],j+my[z]
            if 0<=ii<N and 0<=jj<M and dp[i][j]+table[ii][jj] > dp[ii][jj]:
                dp[ii][jj] = dp[i][j]+table[ii][jj]
                
print( dp[N-1][M-1] )