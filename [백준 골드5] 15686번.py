# 15686번: 치킨 배달
from itertools import combinations
import heapq
import copy

N, M = list( map( int, input().split() ) )
house, chicken = [], []
for i in range(N):
    tmp = list( map( int, input().split() ) )
    for j in range(N):
        if tmp[j] == 1: house.append( [i, j] )
        if tmp[j] == 2: chicken.append( [i, j] )

length = [ [ 0 for i in range(len(chicken)) ] for i in range(len(house)) ]
baseHeap = [ [] for i in range(len(house)) ]
for i, h in enumerate( house ):
    for j, c in enumerate( chicken ):
        length[i][j] = abs( c[0]-h[0] ) + abs( c[1]-h[1] )
        baseHeap[i].append( [length[i][j], j] )
    heapq.heapify( baseHeap[i] )

deleteNum = len( chicken ) - M
if deleteNum > 0:
    result = 1234567890   
    index = [i for i in range( len( chicken ) )]
    for deleteList in combinations( index , deleteNum ):
        tmpHeap = copy.deepcopy( baseHeap )
        tmp = 0
        for i in range( len(house) ):
            while tmpHeap[i][0][1] in deleteList:  heapq.heappop( tmpHeap[i] )
            tmp += tmpHeap[i][0][0]
        result = min( result, tmp )
else:
    result = 0
    for i in range(len(house)): result += baseHeap[i][0][0]
print( result )