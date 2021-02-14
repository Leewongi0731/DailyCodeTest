# 연습문제: 땅따먹기
def solution(land):
    N = len(land)
    dp = [ [0]*4 for i in range(N) ]
    dp[0] = land[0]
    
    for i in range(1, N):
        for j in range(4):
            for z in range(4):
                if j == z: continue
                dp[i][j] = max( dp[i][j], dp[i-1][z]+land[i][j] )
        
    return max( dp[N-1] )