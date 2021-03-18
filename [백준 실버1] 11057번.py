# 11057번: 오르막 수
N = int(input())

dp = [ 1 for i in range(10) ]
length = 1
while length < N:
    preSum = sum(dp)
    for i in range(10):        
        tmp = preSum
        preSum -= dp[i]
        dp[i] = tmp % 10007
        
    length += 1
    
print( sum(dp) % 10007 )