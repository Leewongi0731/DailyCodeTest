# 14226번: 이모티콘
from collections import deque

def solution( S ):
    visited = [ [False for i in range(S*2)] for i in range(S*2) ] # 해당길이, 클립보드 길이
    visited[1][0] = visited[1][1] = visited[2][1] = True
    
    queue = deque()
    queue.append( [2, 1, 2] ) # 현재 갯수, 클립보드 수, cost

    while queue:
        n, clipboard, cost = queue.popleft()
        
        if n == S: return cost
        
        # 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
        if visited[n][n] == False:
            visited[n][n] = True
            queue.append( [n, n, cost+1] )
            
        # 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
        if n + clipboard < S*2 and visited[ n + clipboard ][ clipboard ] == False:
            visited[ n + clipboard ][ clipboard ] = True
            queue.append( [n + clipboard, clipboard, cost+1] )
        
        
        # 화면에 있는 이모티콘 중 하나를 삭제한다.
        if n-1 > 0 and visited[n-1][clipboard] == False:
            visited[n-1][clipboard] = True
            queue.append( [n-1, clipboard, cost+1] )
            
    return -1
######################################################    
S = int(input())
result = solution(S)
print( result )