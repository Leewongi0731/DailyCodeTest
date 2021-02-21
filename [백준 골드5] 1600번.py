# 1600번: 말이 되고픈 원숭이
from collections import deque

def BFS(  ):
    global W,H,K
    if W==1 and H==1: return 0
    
    queue = deque()
    queue.append( [0,0,K,0] ) # i / j / k / count
    visited = [ [[False] * (K+1) for i in range(W) ] for i in range(H) ] # i, j, 남은 K수
    visited[0][0][K] = True
    
    while queue:
        i, j, k, count = queue.popleft()
        
        for z in range(4):
            # 원숭이의 움직임
            mi = i + monkeyMx[z]
            mj = j + monkeyMy[z]
            if 0<=mi<H and 0<=mj<W and table[mi][mj]==0 and visited[mi][mj][k]==False:
                visited[mi][mj][k]=True
                queue.append( [mi,mj,k,count+1] )
                if mi==H-1 and mj==W-1: return count+1
                

        if k>0: 
            # 말로 움직일 수 있을경우
            for z in range(8):
                mi = i + horseMx[z]
                mj = j + horseMy[z]
                if 0<=mi<H and 0<=mj<W and table[mi][mj]==0 and visited[mi][mj][k-1]==False:
                    visited[mi][mj][k-1]=True
                    queue.append( [mi,mj,k-1,count+1] )
                    if mi==H-1 and mj==W-1: return count+1

    return -1
##########################################################################
K = int(input())
W, H = list(map(int, input().split()))
table = [ list(map(int, input().split())) for i in range(H) ]

horseMx = [ -1, -2, -2, -1, +1, +2, +2, +1 ]
horseMy = [ -2, -1, +1, +2, +2, +1, -1, -2 ]
monkeyMx = [ -1, +1, 0, 0 ]
monkeyMy = [ 0, 0, -1, +1 ]

result = BFS()
print( result )