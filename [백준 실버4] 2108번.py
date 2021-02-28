# 2108번: 통계학
from collections import Counter
import sys

N = int(input())

datas = [ int( sys.stdin.readline() ) for i in range(N) ]
datas = sorted( datas )

# 산술평균 
print( round( sum(datas)/N ) )

# 중앙값 
print( datas[N//2] )

# 최빈값 
c = dict( Counter( datas ) )
sortedByValue = sorted( c.items(), key=(lambda x:x[1]), reverse=True )
if len(sortedByValue)==1: print( sortedByValue[0][0] )
elif sortedByValue[0][1]==sortedByValue[1][1]: print( sortedByValue[1][0] )
else: print( sortedByValue[0][0] )
    
# 범위 
print( datas[-1]-datas[0] )