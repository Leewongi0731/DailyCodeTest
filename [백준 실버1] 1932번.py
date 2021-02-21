# 1932번: 정수 삼각형
n = int(input())
datas = [ list(map(int, input().split())) for i in range(n) ]
    
dp = [ [0]*n for i in range(n) ]
dp[0][0] = datas[0][0]

for depth in range(1, n):
    # 양 끝점은 상위의 끝점 하나에만 연결 가능
    dp[depth][0] = datas[depth][0] + dp[depth-1][0]
    dp[depth][depth] = datas[depth][depth] + dp[depth-1][depth-1]
    
    for index in range(1, depth):
        dp[depth][index] = datas[depth][index] + max( dp[depth-1][index-1], dp[depth-1][index] )
        
print( max(dp[n-1]) )