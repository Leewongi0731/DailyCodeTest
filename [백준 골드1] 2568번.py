# 2568번: 전깃줄 - 2
# 최장 증가 부분 수열 (LIS : Longest Increasing Subsequence) 문제
from bisect import bisect_left #이진탐색 코드

N = int(input())
datas = [ [] for i in range(N) ]
for i in range(N):
    datas[ i ] = list(map(int, input().split()))
datas = sorted( datas )

dp = [ ]
save = [  ]
for a, b in datas:
    k = bisect_left(dp, b) #자신이 들어갈 위치 k
    if len(dp) <= k: # b가 가장 큰 숫자라면
        dp.append(b)
        save.append( [ [a, b] ] )
    else:
        dp[k] = b #자신보다 큰 수 중 최솟값과 대체
        save[k].append( [a, b] )
        
        
result = [ a for a, b in save[-1][:-1] ]
now = save[-1][-1]
for i in range( len(save)-2, -1, -1 ):
    for j in range( len(save[i])-1, -1, -1 ):
        if save[i][j][0] < now[0] and save[i][j][1] < now[1]:
            now = save[i][j]
            break
        else:
            result.append( save[i][j][0] )
    
    for z in range(j-1, -1, -1):
        result.append( save[i][z][0] )

result = sorted( result )
print( len(result) )
print('\n'.join( map(str, result)))