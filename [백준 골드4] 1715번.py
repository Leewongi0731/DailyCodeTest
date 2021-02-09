# 1715번: 카드 정렬하기
import heapq

N = int(input())
heap = []
for i in range(N):
    heapq.heappush( heap, int(input()) )
    
result = 0
while len(heap)>1:
    d1 = heapq.heappop(heap)
    d2 = heapq.heappop(heap)
    result += d1 + d2
    heapq.heappush( heap, d1+d2 )
print( result )