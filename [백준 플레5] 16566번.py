# 16566번: 카드 게임
from bisect import bisect_left
import heapq

def possibleIdx( i ):
    if used[i] == i: return i
    else: return possibleIdx( used[i] )
######################################################
N, M, K = list(map(int, input().split()))
cardList = list(map(int, input().split())) + [N+1]
cardList.sort()
used = [ i for i in range(M+1) ]

redCard = list(map(int, input().split()))

redHeap = []
for i, re in enumerate( redCard ):
    heapq.heappush( redHeap, [-re, i] )

result = [ 0 for i in range(K) ]
for _ in range(K):
    re, index = heapq.heappop( redHeap )
    
    targetIndex = bisect_left( cardList, (-re)+1 )
    if targetIndex == M: # impossible
        realIndex = possibleIdx( 0 )
    else:
        realIndex = possibleIdx( targetIndex )
        if realIndex == M:
            realIndex = possibleIdx( 0 )
            
    result[index] = cardList[ realIndex ]
    used[ realIndex ] = used[ targetIndex ] = used[ realIndex+1 ]

for r in result:
    print(r)