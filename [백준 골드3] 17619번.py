# 17619번: 개구리 점프
import sys

N, Q = list(map(int, input().split()))
datas = []
for i in range(N):
    x1,x2,y = list(map(int, sys.stdin.readline().split()))
    datas.append( [x1, x2, y, i] )
datas = sorted( datas )

group = [0 for i in range( N )]
groupRange = [ datas[0][0], datas[0][1] ]
groupNum = 1
group[ datas[0][3] ] = groupNum

for x1, x2, y, i in datas[1:]:
    if groupRange[0] <= x1 <= groupRange[1]:
        groupRange[1] = max( groupRange[1], x2 )
    else:
        groupRange = [ x1, x2 ]
        groupNum += 1    
    group[i] = groupNum
    
for _ in range(Q):
    r1, r2 = list(map(int, sys.stdin.readline().split()))
    if group[r1-1] == group[r2-1]: print( 1 )
    else: print( 0 )