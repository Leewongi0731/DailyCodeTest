# 6087번: 레이저 통신
from collections import deque

W, H = list(map(int, input().split()))

maxVal = 999999999
visited = [ [ [maxVal]*4 for i in range(W)] for i in range(H) ] # i, j, d -> minVal
start = end = None

table = [ ]
for i in range(H):
    table.append( list(input()) )
    for j in range(W):
        if table[i][j]=='C':
            if start==None: start=[i,j]
            else: end=[i,j]
        
        if table[i][j]=='*':
            visited[i][j][0] = visited[i][j][1] = visited[i][j][2] = visited[i][j][3] = -1

# 방향 : 0:아래 / 1:위 / 2:왼 / 3:오른
mx = [-1,1,0,0]
my = [0,0,-1,1]
turnFillter = [ [2,3], [2,3], [0,1], [0,1] ]


#visited[start[0]][start[1]] = 0
stack = deque()
i, j = start[0], start[1]
for z in range(4):
    mi, mj = i + mx[z], j + my[z]
    if 0<=mi<H and 0<=mj<W and table[mi][mj]!='*':
        visited[mi][mj][z] = 0
        stack.append( [mi, mj, z] )

while stack:
    i, j, d = stack[-1]
    popFlag = True
    if i!=end[0] or j!=end[1]:
        # 동일 방향으로 +1
        mi, mj = i + mx[d], j + my[d]
        if 0<=mi<H and 0<=mj<W and visited[mi][mj][d]>visited[i][j][d]:
            visited[mi][mj][d] = visited[i][j][d]
            stack.append( [mi, mj, d] )
            popFlag=False
        
        # 동일방향으로 진행할 수 없을 경우 90도 회전
        if popFlag==True:
            for z in turnFillter[d]:
                mi, mj = i + mx[z], j + my[z]
                if 0<=mi<H and 0<=mj<W and visited[mi][mj][z]>visited[i][j][d]+1:
                    visited[mi][mj][z] = visited[i][j][d]+1
                    stack.append( [mi, mj, z] )
                    popFlag=False
                    break
    if popFlag==True: stack.pop()
    
print( min(visited[end[0]][end[1]]) )