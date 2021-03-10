# 1175번: 배달
from collections import deque

def minDist( start ):
    global N, M
     # i, j, state, dir => visit 여부
    visited = [ [ [ [False, False, False, False] for i in range(4) ] for i in range(M) ] for i in range(N)]
    mx, my = [-1,1,0,0], [0,0,-1,1] # 위 / 아래 / 왼 / 오
    
    queue = deque()
    queue.append( [start[0], start[1], -1, 0, 0] ) # i, j, beforDir, cost, state
    while queue:
        i, j, beforDir, cost, state = queue.popleft()
        print(i, j, beforDir, cost, state)
        if state==3: return cost
        
        for z in range(4):
            if z == beforDir: continue
                
            ii, jj = i+mx[z], j+my[z]
            if 0<=ii<N and 0<=jj<M and table[ii][jj]!='#':
                nextState = state
                if table[ii][jj]=='C': nextState |= target[(ii,jj)]
                
                if visited[ii][jj][nextState][z] == False:
                    visited[ii][jj][nextState][z]=True
                    queue.append( [  ii, jj, z, cost+1, nextState  ] )
                    
    return -1
#################################################
N, M = list(map(int, input().split()))
table = [ list(input()) for i in range(N) ] 
target = {}
start = []
for i in range(N):
    for j in range(M):
        if table[i][j] == 'S': start = [i, j]
        if table[i][j] == 'C': target[ (i,j) ] = len(target)+1

result = minDist( start )
print( result )