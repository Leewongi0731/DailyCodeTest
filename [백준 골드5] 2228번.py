# 2228번: 구간 나누기
def getDp( n, m ):
    if m==0: return 0
    if n<0: return -123456789123
    
    if dp[n][m] == None:
        # 마지막 index가 포함되지 않는 경우로 init
        dp[n][m] = getDp(n-1, m)
        
        if m==1: dp[n][m] = max( dp[n][m], preSum[n] )
        
        for k in range(n, 0, -1):
            # 마지막 index가 포함되고, m번째 집합의 시작이 k일 경우
            # ex) n=10, m=3
            # k=10 [0~8]구간에서 2집합 + [10~10]구간의 합
            # k=9 [0~7]구간에서 2집합 + [9~10]구간의 합
            # ...
            # k=2 [0~0]구간에서 2집합 + [2~10]구간의 합
            # k=1 [0~-1]구간에서 2집합 + [1~10]구간의 합
            dp[n][m] = max( dp[n][m], getDp(k-2, m-1) + preSum[n]-preSum[k-1] )
        
    return dp[n][m]
###############################################################
N, M =list(map(int, input().split()))
preSum = [0 for i in range(N)]
preSum[0] = int(input())
for i in range(1, N):
    data = int(input())
    preSum[i] = preSum[i-1] + data

# dp[N][M] : 0~N index 구간에서 M등분 했을때의 최대 값
dp = [[None for i in range(M+1)] for i in range(N)] 
    
result = getDp( N-1, M )
print( result )