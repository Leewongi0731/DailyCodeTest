# 10844번: 쉬운 계단 수
import copy

N = int(input())

dp = [1 for i in range(12)]
dp[0] = dp[1] = dp[11] = 0
nextDp = [0 for i in range(12)]
length = 1
while length < N:
    for i in range(1, 11):
        nextDp[i] = dp[i-1] + dp[i+1]
        nextDp[i] %= 1000000000
    
    dp = copy.deepcopy( nextDp )
    length += 1

print( sum(dp)%1000000000 )