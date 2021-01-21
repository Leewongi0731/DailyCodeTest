# 20415번: MVP 다이아몬드 (Hard)
N = int(input())
s, g, p, d = list(map(int, input().split()))
rank = input()

dp = [ 0 for i in range(N) ]
guideline = { 'B':[0, s-1], 'S':[s, g-1], 'G':[g, p-1], 'P':[p, d-1], 'D':[d,d*2] }

if rank[0]=='D': dp[0] = d
else: dp[0] = guideline[ rank[0] ][1]
    
for i, r in enumerate( rank[1:] ):
    i = i + 1
    
    if r == 'D':
        dp[ i ] = d
        continue
    
    val = dp[i-1] + dp[i]
    if val < guideline[ r ][ 1 ]: # 등급이 기준보다 작다면, 해당 월의 값을 해당 등급의 최대치로 설정
        dp[i] = guideline[ r ][ 1 ] - dp[i-1]
    elif val > guideline[ r ][ 1 ]: # 등급이 기준보다 크다면, 해당 월을 0으로 설정하고 저번달부터 최대 값으로 변경해감
        dp[ i ] = 0
        dp[ i - 1 ] = guideline[ r ][ 1 ]
        for ii in range( i-1, 0, -1 ):
            if dp[ ii ] + dp[ ii - 1] < guideline[ rank[ii] ][0]:
                dp[ii-1] = guideline[ rank[ii] ][0] - dp[ ii ]
            elif dp[ ii ] + dp[ ii - 1] > guideline[ rank[ii] ][1]:
                dp[ii-1] = guideline[ rank[ii] ][1] - dp[ ii ]
            else:  # 등급안에 값이 들어갈 경우 그 이전은 이미 최대치 임으로 그만 변경함
                break
print( sum(dp) )