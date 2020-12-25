# 17268번: 미팅의 저주
import sys
sys.setrecursionlimit(10**6)

def sol(x):
    if df[ x ] != -1:
        return df[ x ]
    
    if df[ x - 2 ] == -1:
        df[ x - 2 ] = sol( x - 2 )
    
    re = 0
    re += df[ x - 2 ] * 2 # 기준점으로 좌/우 결합경우
    
    for left in range( 2, x-2, 2 ):
        right = x - 2 - left
        re += ( df[ left ] * df[ right ] ) % 987654321
    return re % 987654321


N = int(input())
df = [ -1 for i in range(N+1) ]
df[ 2 ] = 1
df[ 4 ] = 2
df[ 6 ] = 5

print( sol( N ) )