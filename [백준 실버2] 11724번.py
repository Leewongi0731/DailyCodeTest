# 11724번: 연결 요소의 개수
from collections import deque
import sys

def BFS(node):
    queue = deque()
    queue.append( node )
    while queue:
        node = queue.popleft()
        
        for nextNode, isLink in enumerate(graph[node]):
            if isLink and visited[nextNode] == False:
                visited[nextNode] = True
                queue.append( nextNode )
##########################################
N, M = list( map(int, input().split()) )
graph = [ [0]*(N+1) for i in range(N+1) ]
for _ in range(M):
    u, v = list(map(int, sys.stdin.readline().split()))
    graph[u][v] = graph[v][u] = 1
    
visited = [ False for i in range(N+1) ]
count = 0
for node in range(1, N+1):
    if visited[node] == False:
        visited[node] = True
        BFS(node)
        count += 1
print( count )