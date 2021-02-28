# 2206번: 벽 부수고 이동하기
from collections import deque

def BFS( N, M ):
    if N==1 and M==1: return 1
    
    queue = deque()
    queue.append( [ 0, 0, 1, False ] ) # i , j , count, 이전에 벽을 부셨는지 Flag
    visited = [ [ [False, False] for i in range(M) ] for i in range(N) ] # i, j, 벽 Flag
    visited[0][0][False] = True
    mx, my = [-1,1,0,0], [0,0,-1,1]
    
    while queue:
        i, j, count, flag = queue.popleft()
        
        for z in range( 4 ):
            mi,mj=i+mx[z], j+my[z]
            if 0<=mi<N and 0<=mj<M:
                if table[mi][mj]==0 and visited[mi][mj][flag]==False:
                    visited[mi][mj][flag]=True
                    queue.append( [mi,mj,count+1,flag] )
                if table[mi][mj]==1 and flag==False:                    
                    visited[mi][mj][True]=True
                    queue.append( [mi,mj,count+1,True] )
                
                if mi==N-1 and mj==M-1: return count+1

    return -1
########################################
N, M = list(map(int, input().split()))
table = [ list(map(int, list(input()))) for i in range(N) ]
print( BFS(N, M) )