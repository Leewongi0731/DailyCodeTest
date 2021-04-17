# 20926번: 얼음 미로
# 2021 ICPC Sinchon Winter Algorithm Camp Contest - 초급 : G

import sys
from collections import deque

MAX_VAL = sys.maxsize

W, H = list(map(int, input().split()))
table = [ list(input()) for i in range(H) ]

costs = [ [MAX_VAL for i in range(W)] for i in range(H) ]
target = []
queue = deque()
for i in range(H):
    for j in range(W):
        if table[i][j] not in ['T', 'R', 'H', 'E']:
            table[i][j] = int(table[i][j])
            
        if table[i][j] == 'T': # 시작 위치
            queue.append( [i,j,0] )
            table[i][j] = costs[i][j] = 0
        
        elif table[i][j] == 'E': # 도착 점
            target = [i,j]
        
mx ,my = [-1,1,0,0], [0,0,-1,1]
while queue:
    i, j, c = queue.popleft()
    if costs[i][j] != c: continue
        
    for z in range(4):
        tmpC = c
        ii, jj = i, j
        
        while True:
            ii, jj = ii+mx[z], jj+my[z]
            if 0<=ii<H and 0<=jj<W and table[ii][jj] not in ['R', 'H', 'E']:
                tmpC += table[ii][jj]
            else:
                break
       
        if 0<=ii<H and 0<=jj<W:
            if table[ii][jj]=='R':
                ii, jj = ii-mx[z], jj-my[z]
                if costs[ii][jj] > tmpC:
                    costs[ii][jj] = tmpC
                    queue.append( [ii,jj,tmpC] )
            
            elif table[ii][jj]=='H': # out
                pass
                
            elif table[ii][jj]=='E': # success
                costs[ii][jj] = min( costs[ii][jj], tmpC )
        else: # out of table
            pass
        
if costs[ target[0] ][ target[1] ] == MAX_VAL: print( -1 )
else: print( costs[ target[0] ][ target[1] ] )