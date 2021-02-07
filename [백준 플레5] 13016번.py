# 13016번: 내 왼손에는 흑염룡이 잠들어 있다
from collections import deque
import heapq
import sys
import copy

N = int(input())
graph = {key:{} for key in range(1, N+1)}
for i in range(N-1):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    graph[a][b] = c
    graph[b][a] = c

saveParent = [ 0 for i in range(N+1) ]
costGraph = [ [] for i in range(N+1) ] # 자신의 자식들에게 오는 cost/index를 maxHeap으로 저장

visited = [0 for i in range(N+1)]
visited[1] = 1
stack = deque()
stack.append( 1 )
while stack: # DFS
    top = stack[-1]
    findNext = False
    for nextNode in graph[top].keys():
        if visited[ nextNode ] == 0:
            findNext = True
            visited[ nextNode ] = 1
            saveParent[nextNode] = top # index
            stack.append( nextNode )
            break
            
    if findNext == False:
        parent = saveParent[top]
        if parent != 0:
            # 가장큰 cost, index
            if costGraph[ top ] == []: cost = [ -graph[top][parent], top] # Leaf노드라면, 자기와 parent와의 cost만을 반환
            else:  cost = [ costGraph[top][0][0]-graph[top][parent], top] # Leaf가 아니라면, 자기의 자식들 중 가장 큰 값과 parent와의 cost를 합쳐 반환
                
            heapq.heappush( costGraph[ parent ], cost )
        stack.pop()
        
        
result = [0 for i in range(N+1)]
visited = [0 for i in range(N+1)]
visited[1] = 1
queue = deque()
queue.append( 1 )
while queue: # BFS
    q = queue.popleft()
    
    # parent 최대값
    parent = saveParent[q]
    if parent != 0:
        if len( costGraph[parent] ) > 1: # 형제노드가 있을경우
            if costGraph[parent][0][1] == q: # 자기가 최대 값이라면, 2번째로 큰 것을 추가
                tmp =copy.deepcopy( costGraph[parent] )
                heapq.heappop( tmp )
                cost = [ tmp[0][0]-graph[q][parent], parent ] 
            else: # 자기가 최대가 아니라면, 가장 큰 것을 추가
                cost = [ costGraph[parent][0][0]-graph[q][parent], parent ]
            heapq.heappush( costGraph[ q ], cost )
        else: # 부모와의 연결고리가 자기밖에 없는 경우
            cost = [ -graph[q][parent], parent]
            heapq.heappush( costGraph[ q ], cost )
                                    
    # 최대값
    if len( costGraph[q] ) != 0: # 자기 위치에서 가장 멀리갈 수 있는 곳을 선택
        result[q] = max( result[q], -costGraph[q][0][0]  )
    
    for nextNode in graph[q].keys():
        if visited[ nextNode ] == 0:
            visited[ nextNode ] = 1
            queue.append( nextNode )

for r in result[1:]:
    print( r )