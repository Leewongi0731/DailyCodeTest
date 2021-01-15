# 12865번: 평범한 배낭
N, K = list(map(int, ibbnput().split()))
items = [ list(map(int, input().split())) for iN, K = list(map(int, input().split()))
items = [ list(map(int, input().split())) for i in range(N) ]

dp = [0 for i in range(K+1)]

for w, v in items:
    for i in range(K, w-1, -1):
        dp[i] = max( [dp[i], dp[i-w] + v] )
        
print( dp[-1] ) in range(N) ]