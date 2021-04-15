# 20925번: 메이플스토리
# 2021 ICPC Sinchon Winter Algorithm Camp Contest - 초급 : E

import sys

N, T = list(map(int, input().split()))

dp = [ [0 for i in range(N)] for i in range(T) ]
datas = []
for i in range(N):
    c, e = list(map(int, sys.stdin.readline().split()))
    datas.append( [c,e] )
    if c==0: dp[0][i] = e

costs = [ list(map(int, sys.stdin.readline().split())) for i in range(N) ]
for t in range(1, T):
    for nowNode in range(N):
        if dp[t-1][nowNode] != 0: dp[t][nowNode] = dp[t-1][nowNode] + datas[nowNode][1]
        
        for beforNode in range(N):
            beforT = t-costs[beforNode][nowNode]
            if beforT>=0 and dp[beforT][beforNode]>=datas[nowNode][0]:
                dp[t][nowNode] = max( dp[t][nowNode], dp[beforT][beforNode] )

print( max(dp[T-1]) )