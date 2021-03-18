# 1520번: 내리막 길
M, N = list(map(int, input().split()))
table = [ list(map(int, input().split())) for i in range(M) ]

datas = []
for i in range(M):
    for j in range(N):
        datas.append( [table[i][j], i, j] )
datas = sorted( datas, reverse=True ) # 큰값 -> 작은 값 순으로 정렬


dp = [ [0 for i in range(N)] for i in range(M) ]
dp[0][0] = 1
mx, my = [-1,1,0,0], [0,0,-1,1]
for data, i, j in datas:
    for z in range(4):
        ii,jj=i+mx[z],j+my[z]
        if 0<=ii<M and 0<=jj<N and data>table[ii][jj]: 
            # 큰값에서 작은값 이동 가능한 경우
            # 현재 큰값(i,j)에서 작은값(ii,jj)로 이동할 수 있는 방법은 dp[i][j]임
            dp[ii][jj] += dp[i][j]
    
print( dp[M-1][N-1] )