# 11658번: 구간 합 구하기 3
# TwoDimension FenwickTree 문제
import sys

def updateTwoDimensionFenwickTree( i, j, diff ):
    global N
    
    x, y = i, j
    while x <= N:
        y = j
        while y <= N:
            fenwickTree[x][y] += diff
            y += (y & -y)
        x += (x & -x)
        
def getSumTwoDimensionFenwickTree( i, j ):
    global N
    sumV = 0
    
    x, y = i, j
    while x > 0:
        y = j
        while y > 0:
            sumV += fenwickTree[x][y]
            y -= (y & -y)
        x -= (x & -x)

    return sumV
######################################################
N, M = list(map(int, input().split()))
datas = []
fenwickTree = [ [ 0 for i in range(N+1) ] for i in range(N+1) ]

for i in range(1, N+1):    
    data = list(map(int, sys.stdin.readline().split()))
    datas.append( data )
    for j in range(1, N+1):
        updateTwoDimensionFenwickTree( i, j, data[j-1] )
        

for _ in range(M):
    query = list(map(int, sys.stdin.readline().split()))
    
    if query[0] == 0:  # (x,y)를 c로 변경
        x, y, c = query[1], query[2], query[3]
        
        beforData = datas[x-1][y-1]
        afterData = c
        diff = afterData - beforData
        
        updateTwoDimensionFenwickTree( x, y, diff )
        
        datas[x-1][y-1] = afterData

        
    else: # (x1,y1) ~ (x2,y2)범위 합
        x1, y1, x2, y2 = query[1], query[2], query[3], query[4]
        
        bigRangeSum = getSumTwoDimensionFenwickTree( x2, y2 )
        leftRangeSum = getSumTwoDimensionFenwickTree( x2, y1-1 ) 
        topRangeSum = getSumTwoDimensionFenwickTree( x1-1, y2 ) 
        smallRangeSum = getSumTwoDimensionFenwickTree( x1-1, y1-1 )
        
        rangeSum = bigRangeSum - leftRangeSum - topRangeSum + smallRangeSum
        print( rangeSum )