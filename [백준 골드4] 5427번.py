# 5427번: 불
# 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동할 수 없다. 
# 상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동할 수 있다.
from collections import deque

T = int(input())
for _ in range(T):
    W, H = list(map(int, input().split()))
    table = [ list(input()) for i in range(H) ]
    
    fire = []
    pos = []
    for i in range(H):
        for j in  range(W):
            if table[i][j] == '*': fire.append( [i,j,0] )
            if table[i][j] == '@':
                table[i][j] = '.'
                pos = [i,j]
    
    visited = [[ -1 for i in range(W) ]for i in range(H)]
    visited[pos[0]][pos[1]] = 0

    mx, my = [-1,1,0,0], [0,0,-1,1]
    
    queue = deque()
    queue.append( pos )
    
    result = "IMPOSSIBLE"
    while queue:
        i, j = queue.popleft()
        time = visited[i][j]
        
        if len(fire) != 0 and fire[0][2]==time:
            # fire update
            newFire = []
            for fi, fj, t in fire:
                for z in range(4):
                    mfi, mfj = fi+mx[z], fj+my[z]
                    if 0<=mfi<H and 0<=mfj<W and table[mfi][mfj]=='.':
                        table[mfi][mfj]='*'
                        newFire.append( [mfi, mfj, time+1] )
            
            fire = newFire
        
        for z in range(4):
            mi, mj = i+mx[z], j+my[z]
            if 0<=mi<H and 0<=mj<W:
                if table[mi][mj]=='.' and visited[mi][mj]==-1: # 이동 가능하고, 이전에 이동한 적이 없다면 이동!
                    visited[mi][mj] = time+1
                    queue.append( [mi,mj] )
            else:
                result = time+1
                break
        
        if result != "IMPOSSIBLE": break
            
    print( result )