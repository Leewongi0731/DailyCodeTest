# 1260번: DFS와 BFS
from collections import deque

N, M, V = list( map(int, input().split()) )
graph = [ [0 for j in range(N)] for i in range(N) ]
for i in range(M):
    a, b = list( map(int, input().split()) )
    graph[ a-1 ][ b-1 ] = 1
    graph[ b-1 ][ a-1 ] = 1
    
# DFS
stack = deque()
stack.append( V-1 )
visited = [0 for j in range(N)]
visited[V-1] = 1
result = [V]
while stack:
    v = stack[-1]
    
    findNext = False
    for nextV, link in enumerate( graph[ v ] ):
        if link == 1 and visited[nextV] == 0:
            stack.append( nextV )
            visited[nextV] = 1
            result.append( nextV+1 )
            findNext = True
            break
            
    if findNext == False:
        stack.pop()
print(' '.join( map(str, result)))

# BFS
queue = deque()
queue.append( V-1 )
visited = [0 for j in range(N)]
visited[V-1] = 1
result = [V]
while queue:
    v = queue.popleft()

    for nextV, link in enumerate( graph[ v ] ):
        if link == 1 and visited[nextV] == 0:
            queue.append( nextV )
            visited[nextV] = 1
            result.append( nextV+1 )
print(' '.join( map(str, result)))