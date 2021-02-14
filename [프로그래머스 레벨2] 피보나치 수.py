# 연습문제: 피보나치 수
import sys
sys.setrecursionlimit( 10**9 )
dp = [None for i in range(100001)]
dp[0], dp[1] = 0, 1

def solution(n):
    if dp[n] == None: dp[n] = (solution(n-2) + solution(n-1) ) % 1234567
    return dp[n]
