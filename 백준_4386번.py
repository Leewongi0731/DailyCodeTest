# 4386번: 별자리 만들기
import math
def getLen( point1, point2 ):
    length = math.sqrt(( point1[0] - point2[0] ) * ( point1[0] - point2[0] ) + ( point1[1] - point2[1] ) * ( point1[1] - point2[1] ) )
    return round(length,2)
############################################################
n = int(input())
graph = [ [0 for i in range(n)]  for j in range(n)]
points = []
for i in range(n):
    point = list(map(float, input().split()))
    j = 0
    for p in points:
        graph[ i ][ j ] = getLen( p, point )
        graph[ j ][ i ] = graph[ i ][ j ]
        j += 1
    points.append( point )
    
totalLen = 0

visited = [ 0 for i in range(n) ]
visited[0] = 1
minLenList = graph[ 0 ]
minLenList[0] = 1000000000000

for _ in range(n-1):
    unVisitedLen = [ minLenList[i] for i, v in enumerate( visited ) if v == 0 ]
    minLen = min( unVisitedLen )
    nextIndex = minLenList.index( minLen )
    minLenList[ nextIndex ] = 1000000000000
    
    visited[ nextIndex ] = 1
    totalLen += minLen
    
    # change minLenList
    for i in range(n):
        if visited[i] == 1:
            continue

        if minLenList[i] > graph[ nextIndex ][ i ]:
            minLenList[i] = graph[ nextIndex ][ i ]
            
print( totalLen )