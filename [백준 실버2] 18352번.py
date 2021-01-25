# 18352번: 특정 거리의 도시 찾기
from collections import deque
import sys

MAX_LEN = sys.maxsize

N, M, K, X = list(map(int, input().split()))
graph = [ [] for i in range(N+1) ]
for _ in range(M):
    A,B = list(map(int, sys.stdin.readline().split()))
    graph[A].append( B )

visited = [-1]*(N+1)
visited[X] = 0
queue = deque()
queue.append( X )
result = []
while queue:
    q = queue.popleft()
    
    if visited[q] > K: break
    
    for nextNode in graph[q]:
        if visited[ nextNode ] == -1:
            visited[ nextNode ] = visited[q] + 1
            if visited[ nextNode ] == K: result.append( nextNode )
            queue.append( nextNode )

result = sorted( result )
if len(result) == 0: print(-1)
else: print( '\n'.join(map(str, result)) )