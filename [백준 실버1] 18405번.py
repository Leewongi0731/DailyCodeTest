# 18405번: 경쟁적 전염
from collections import deque

N, K = list(map(int, input().split()))
virus = [ [] for i in range(K+1) ]
table = [ [] for i in range(N) ]
for i in range(N):
    table[i] = list(map(int, input().split()))
    for j in range(N):
        if table[i][j] != 0:
            virus[ table[i][j] ].append( [i,j] )    
S, X, Y = list(map(int, input().split()))

mx = [-1,1,0,0]
my = [0,0,-1,1]
for s in range(S):
    for v in range(1, K+1):
        update = []
        for i, j in virus[v]:
            for z in range(4):
                ii, jj = i + mx[z], j + my[z]
                if 0<=ii<N and 0<=jj<N and table[ii][jj]==0:
                    table[ii][jj] = v
                    update.append( [ii,jj] )
        virus[v] = update
    
print( table[X-1][Y-1] )