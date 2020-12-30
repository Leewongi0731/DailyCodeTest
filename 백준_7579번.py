# 7579번: 앱
N, M = list(map(int, input().split()))
memorys = list(map(int, input().split()))
costs = list(map(int, input().split()))
totalCost = sum(costs)

dp = [ 0 for i in range(totalCost + 1) ] # index : cost, value : memory

for i in range(N):
    for j in range( totalCost, costs[i] - 1, -1 ):
        dp[ j ] = max( dp[j], dp[ j - costs[i] ] + memorys[ i ] )
        
for cost, memory in enumerate(dp):
    if memory >= M:
        print(cost)
        break