# 2146번: 다리 만들기
from collections import deque
import copy

N = int(input())
table = [ list(map(int, input().split())) for i in range(N) ]

mx = [-1,1,0,0]
my = [0,0,-1,1]

numbering = 2
for i in range(N):
    for j in range(N):
        if table[i][j] == 1:
            table[i][j] = numbering
            
            queue = deque()
            queue.append( [i,j] )          
            while queue:
                ii, jj = queue.popleft()
                
                for z in range(4):
                    mi, mj = ii + mx[z], jj + my[z]
                    if 0<=mi<N and 0<=mj<N and table[mi][mj]==1:
                        table[mi][mj] = numbering
                        queue.append( [mi,mj] )
            numbering += 1

result = 1000000000000
for i in range(N):
    for j in range(N):
        if table[i][j] != 0:
            islandNum = table[i][j]
            visited = copy.deepcopy( table )
            
            queue = deque()
            for z in range(4): # 주변에 바다가 있을경우 ( 시작이 가능한 지점 )
                mi, mj = i + mx[z], j + my[z]
                if 0<=mi<N and 0<=mj<N and visited[mi][mj]==0:
                    visited[mi][mj] = 1
                    queue.append( [mi,mj,1] )
            
            while queue:
                ii, jj, c = queue.popleft()                
                if c > result: break
                findFlag = False
                
                for z in range(4):
                    mi, mj = ii + mx[z], jj + my[z]
                    if 0<=mi<N and 0<=mj<N and visited[mi][mj]!=1:
                        if visited[mi][mj] == 0:
                            visited[mi][mj] = 1
                            queue.append( [mi,mj,c+1] )
                        elif visited[mi][mj] != islandNum:
                            findFlag = True
                            break
                            
                if findFlag: 
                    result = min( result, c )
                    break
print( result )