# Summer/Winter Coding: 쿠키 구입
from bisect import bisect_left
import sys
sys.setrecursionlimit( 10**9 )

def getDp(l, r, cookie, preSum, dp):
    if l >= r: return 0
    
    if dp[l][r] == -1:
        dp[l][r] = 0
        
        totalSum = preSum[r] - preSum[l-1]
        if totalSum % 2 == 0:
            targetSum = totalSum // 2

            findIndex = bisect_left( preSum, targetSum + preSum[l-1] )
            if findIndex < len(preSum) and preSum[findIndex] == targetSum + preSum[l-1]:
                dp[l][r] = targetSum
                return dp[l][r]
    
        dp[l][r] = max( getDp(l+1, r, cookie, preSum, dp),
                       getDp(l, r-1, cookie, preSum, dp) )
    
    return dp[l][r]

def solution(cookie):
    N = len(cookie)
    preSum = [0]
    for c in cookie:
        preSum.append( preSum[-1]+c )
    
    l, r = 1, N
    dp = [ [ -1 for i in range(N+1) ] for i in range(N+1) ]
    answer = getDp( l, r, cookie, preSum, dp)
    return answer