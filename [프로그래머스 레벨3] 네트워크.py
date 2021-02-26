# DFS/BFS: 네트워크
from collections import deque

def solution(n, computers):
    visited = [ False for i in range(n) ]

    answer = 0
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            queue = deque()
            queue.append( i )
            
            while queue:
                index = queue.popleft()
                for nextIndex in range(n):
                    if computers[index][nextIndex]==True and visited[nextIndex]==False:
                        visited[nextIndex]=True
                        queue.append( nextIndex )
            answer+=1
    return answer