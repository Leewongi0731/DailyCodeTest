# 14502번: 연구소
from itertools import combinations
from collections import deque

def countVirus():
    cnt = 0
    q = deque(virus)
    visited = [[0]*M for i in range(N)]
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    cnt += 1
                    q.append((nx, ny))
    return cnt
######################################################################################    
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(N)]
virus, wall, blank = [], [], []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            blank.append((i, j))
        if graph[i][j] == 1:
            wall.append((i, j))
        if graph[i][j] == 2:
            virus.append((i, j))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
max_value = 0

for combi in combinations(blank, 3): # 0 지점중 3개를 무작위로 뽑아서 벽으로 만들고 안전지역 넓이를 측정
    for i, j in combi: graph[i][j] = 1
        
    virusCount = countVirus()
    max_value = max(max_value, len(blank) - 3 - virusCount )
    
    for i, j in combi: graph[i][j] = 0

print(max_value)