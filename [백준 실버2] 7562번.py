# 7562번: 나이트의 이동
from collections import deque

def getMinCost( now, target ):
    global I
    queue = deque()
    queue.append( now + [0] )
    visited = [ [False]*I for i in range(I) ]
    visited[now[0]][now[1]] = True
    
    while queue:
        x, y, c = queue.popleft()
        
        if x == target[0] and y == target[1]: return c
        
        for z in range(8):
            nx = x + mx[z]
            ny = y + my[z]
            if 0<=nx<I and 0<=ny<I and visited[nx][ny]==False:
                visited[nx][ny]=True
                queue.append( [nx,ny,c+1] )
    return -1
        
######################################################

T = int(input())

mx = [ -1, -2, -2, -1, +1, +2, +2, +1 ]
my = [ -2, -1, +1, +2, +2, +1, -1, -2 ]

for _ in range(T):
    I = int(input())
    now = list( map(int, input().split()) )
    target = list( map(int, input().split()) )
    
    cost = getMinCost( now, target )
    
    print( cost )