# 1987번: 알파벳
from collections import deque
def dfs(i, j, s, c):
    global result, R, C
    result = max(result, c)
    
    for z in range(4):
        ii = i + mx[z]
        jj = j + my[z]
        
        if 0 <= ii < R and 0 <= jj < C:
            ns = s | ( 1 << (ord(graph[ii][jj]) - ord('A')) )
            
            if s != ns:
                if ns not in visited[ii][jj].keys(): # 해당 지점을 동일 state에서 방문했던적 있었으면 방문 필요 X
                    dfs( ii, jj, ns, c+1 )
                    visited[ii][jj][ns]=1
                
########################################################################
    
R, C = list(map(int, input().split()))
graph = [ list(input()) for i in range(R)]
visited = [ [ {} for i in range(C) ] for i in range(R) ] # graph 각 지점에 방문 state 저장

mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]
result = 0
state = 1 << (ord(graph[0][0]) - ord('A'))

dfs( 0,0,state,1 )
        
print( result )