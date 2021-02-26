# 11066번: 파일 합치기

T = int(input())
for _ in range(T):
    K = int(input())
    datas = list(map(int, input().split()))
    preSum = [ datas[0] ]
    for i in range(1, K): preSum.append( preSum[-1] + datas[i] )
    
    # dp 초기화
    # start, end가 같으면 cost 0
    dp = [ [99999999 for i in range(K)] for i in range(K) ]
    for i in range(K): dp[i][i] = 0
        
    for start in range(K-2, -1, -1):
        for end in range(start+1, K):
            # start~end 지점을 두개로 나누었을때 가장 합쳐지는데 가장 작은 값
            dp[start][end] =  min( [ dp[start][mid] + dp[mid+1][end] for mid in range( start, end ) ] )
            
            # 중간지점이 어디든, 두개의 그룹을 합치는데 필요한 cost
            if start == 0: dp[start][end] += preSum[end]
            else: dp[start][end] += preSum[end] - preSum[start-1]
            
    print( dp[0][K-1] )