# 10942번: 팰린드롬?
import sys

N = int(input())
dp = [ [ [0,-1,-1] for i in range(N)] for j in range(N) ]
datas = list(map(int, sys.stdin.readline().split()))
M = int(input())
for _ in range(M):
    # 시간 제한이 빡세서, 일반 input()으로 받으면 시간초과됨..
    S, E = list(map(int, sys.stdin.readline().split()))
    S -= 1
    E -= 1
    
    if S == E:
        print(1)
        continue
    
    if ( E - S ) % 2 == 1:
        s = ( E + S ) // 2
        e = s + 1
    else:
        s = ( E + S ) // 2
        e = s
    
    if dp[s][e][0] == 1: # 가운데 시작지점에서, 최대 확인된 팰린드롬 까지 시작점 이동
        ss = dp[s][e][1]
        ee = dp[s][e][2]
    else:
        ss = s
        ee = e
        
    palindrome = True
    for i in range( 0, ss-S+1, +1 ):
        if datas[ss-i] == datas[ee+i]: 
            continue
        else:
            palindrome = False
            break
            
    if palindrome:
        if S < ss: # 시작지점에서 더 긴 팰린드룸을 발견했다면 업데이트.
            dp[s][e] = [1, S, E]
        print( 1 )
    else:
        if ss-i+1 < ee+i-1: # 실패였다면 -> 바로 그 전까지는 팰린드롬 이라는 것.-> 업데이트.
            dp[s][e] = [1, ss-i+1, ee+i-1]
        print( 0 )