# 5014번: 스타트링크
from collections import deque

F, S, G, U, D = list(map(int, input().split()))
visited = [ -1 for i in range(F+1) ]
visited[S]=0

queue = deque()
queue.append( S )
while queue:
    now = queue.popleft()
    if now == G: break
    
    # 위 버튼
    if now+U<F+1 and visited[now+U]==-1:
        visited[now+U]=visited[now]+1
        queue.append( now+U )
    
    # 아래 버튼
    if 1<=now-D and visited[now-D]==-1:
        visited[now-D]=visited[now]+1
        queue.append( now-D )
        
if visited[G]==-1: print('use the stairs')
else: print( visited[G] )