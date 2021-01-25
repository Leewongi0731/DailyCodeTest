# 16234번: 인구 이동
from collections import deque

def BFS(i, j):
    global N, L, R
    queue = deque( )
    queue.append( [i,j] )

    while queue:
        i, j = queue.popleft()

        for x in range(4):
            ii, jj = i+mx[x], j+my[x]
            if ii >= 0 and ii < N and jj >= 0 and jj < N and visited[ii][jj] == 0:
                gap = abs( graph[i][j] - graph[ii][jj] )
                if L <= gap and gap <= R:
                    group[-1][0] += graph[ii][jj]
                    group[-1][1].append( [ii, jj] )
                    queue.append( [ii, jj] )
                    visited[ii][jj] = 1
######################################################################################  

N, L, R = list( map( int, input().split() ) )
graph = [ list( map( int, input().split() ) ) for i in range(N) ]
mx = [-1,1,0,0]
my = [0,0,-1,1]

result = 0
while True:
    visited = [ [0]*N for i in range(N) ]
    group = []
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                group.append( [graph[i][j], [ [i,j] ]  ] )
                visited[i][j] = 1
                BFS( i, j )

    if len(group) == N**2: break

    for groupIndex in range( len(group) ):
        avg = group[groupIndex][0] // len( group[groupIndex][1] )
        for i, j in group[groupIndex][1]: graph[i][j] = avg

    result += 1
print( result )