# 1655번: 가운데를 말해요
# binary search, insert 조합으로 하면 시간초과. 
# 배열의 item추가 시간복잡도를 줄이기 위해 좌(maxHeap), 우(minHeap)으로 구현
import sys
import heapq

N = int(input())
mid = int(input())
print( mid )

# 항상 len( left ) = len(right) or len( left ) = len( right ) + 1
left = [] # 가장 큰 값 -> maxHeap
right = [] # 가장 작은 값 -> minHeap
for _ in range(N-1):
    item = int( sys.stdin.readline() )
    
    if mid > item: heapq.heappush( left, -item )
    else: heapq.heappush( right, item )

    if len( left ) > len( right ):
        heapq.heappush( right, mid )
        mid = -heapq.heappop( left )
    elif len( left ) + 1 < len( right ):
        heapq.heappush( left, -mid )
        mid = heapq.heappop( right )
    
    print( mid )