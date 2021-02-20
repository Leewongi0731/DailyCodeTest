# 2667번: 단지번호붙이기
from collections import deque

def BFS(i, j):
    global N
    queue = deque()
    queue.append( [i,j] )
    count = 1
    while queue:
        i, j = queue.popleft()
        
        for z in range(4):
            mi = i + mx[z]
            mj = j + my[z]
            
            if 0<=mi<N and 0<=mj<N and table[mi][mj]==1:
                table[mi][mj] = 2
                queue.append( [mi, mj] ) 
                count += 1
    return count
######################################################
N = int(input())
table = [ list(map( int, list(input()) )) for i in range(N) ]
mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]

counts = []
for i in range(N):
    for j in range(N):
        if table[i][j] == 1:
            table[i][j] = 2
            count = BFS(i, j)
            counts.append( count )
            
counts = sorted( counts )
print( len(counts) )
for count in counts:
    print( count )