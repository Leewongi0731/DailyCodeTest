# 16946번: 벽 부수고 이동하기 4
from collections import deque

def dfs(i, j, groupNum):
    count = 1
    queue = deque()
    queue.append( [i, j] )
    visited[i][j] = groupNum
    
    while queue:
        i, j = queue.popleft()
        
        for z in range(4):
            ii = i + mx[z]
            jj = j + my[z]
            
            if 0 <= ii < N and 0 <= jj < M and graph[ii][jj]==0 and visited[ii][jj]==0:
                queue.append( [ii, jj] )
                visited[ii][jj] = groupNum
                count += 1
    return count
 
###################################################################################################

N, M = list(map(int, input().split()))
graph = [ list(map(int, list(input()))) for i in range(N) ]

visited = [ [0]*M for i in range(N) ]
mx = [-1,1,0,0]
my = [0,0,-1,1]
groupCount = {}
groupNum= 1
for i in range(N): # 0의 군집갯수 세서 Dict에 저장
    for j in range(M):
        if graph[i][j] == 0 and visited[i][j] == 0:
            count = dfs( i, j, groupNum )
            groupCount[ groupNum ] = count
            groupNum += 1


result = [ [0]*M for i in range(N) ]
for i in range(N): # 벽위치에서 주변의 군집의 groupNum을 따라서 주변 0갯수를 셈
    for j in range(M):
        if graph[i][j] == 1:
            groupList = []
            for z in range(4):
                ii = i + mx[z]
                jj = j + my[z]
                if 0 <= ii < N and 0 <= jj < M and graph[ii][jj]==0:
                    groupList.append( visited[ii][jj] )
            
            count = 1 # 벽 위치 추가
            for groupNum in set(groupList):
                count += groupCount[ groupNum ]
            
            result[i][j] = count % 10
    print( ''.join(map(str, result[i])) )