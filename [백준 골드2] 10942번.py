# 10942번: 팰린드롬?
import sys

N = int(input())
dp = [[0] * N for i in range(N)]
datas = list(map(int, sys.stdin.readline().split()))

for length in range(N):
    # 길이가 1부터 N까지의 팰린드롬을 순서대로 찾아 dp에 저장
    for start in range(N):
        end = start + length
        if end >= N: break
            
        if start == end:
            dp[start][end]=1
            continue
            
        if start + 1 == end:
            if datas[start] == datas[end]:
                dp[start][end] = 1
                continue
            
        if datas[start] == datas[end] and dp[start+1][end-1]:
            # ex) 0 0 1 1 0 0 -> 맨 외각의 0, 0이 같고, dp[1][4]가 팰린드롬이라면, 해당 문자는 팰린드롬.
            dp[start][end] = 1
    
M = int(input())
for i in range(M):
    S, E = map(int, sys.stdin.readline().split())
    print(dp[S - 1][E - 1])