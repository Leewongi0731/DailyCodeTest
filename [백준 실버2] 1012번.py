# 1012번: 유기농 배추
from collections import deque
T = int(input())

for _ in range(T):
    M, N, K = list( map(int, input().split()) )
    
    graph = [ [0 for j in range(M)] for i in range(N) ]
    for i in range(K):
        y, x = list( map(int, input().split()) )
        graph[ x ][ y ] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    result = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0 or graph[i][j] == 2:
                continue

            result += 1

            queue = deque()
            queue.append( [i, j] )
            while queue:
                x, y = queue.popleft()
                graph[x][y] = 2

                for z in range(4):
                    mx = x + dx[z]
                    my = y + dy[z]

                    if mx >= 0 and my >= 0 and mx < N and my < M and graph[mx][my] == 1:
                        queue.append( [mx, my] )
                        graph[mx][my] = 2
    print( result )