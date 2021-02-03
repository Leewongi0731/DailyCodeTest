# 1799번: 비숍

def getColor( N,i,j ):
    idx = i*N + j
    if N%2 == 0:
        # 흑 백
        # 백 흑
        if i%2==1:
            if j%2==1: return True
            else: return False
        else:
            if j%2==1: return False
            else: return True
    else:
        # 흑 백 흑
        # 백 흑 백
        # 흑 백 흑
        if idx%2==0: return True
        else: return False
        
def isPosible( p1, p2 ):
    i1, j1 = p1[0], p1[1]
    i2, j2 = p2[0], p2[1]
    
    for z in range(4): # 방향
        c = 1
        while True:
            ii = i1 + mx[z]*c
            jj = j1 + my[z]*c
            if 0 <= ii < N and 0 <= jj < N:
                if ii == i2 and jj == j2: # 충돌
                    return False
            else: break
            c += 1
    return True 
        
def getImpossibleBitMask(positions):
    impossibleBitMask = [ 0 for i in range(len(positions)) ]
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            if not isPosible( positions[i], positions[j] ): # 둘이 같이 사용하는 것이 불가능 하다면,
                 impossibleBitMask[i] |= (1 << j)
    return impossibleBitMask

def dfs( i, impossible ):
    if i > len(pos)-1: return 0        
    if i == len( pos ) -1:
        if impossible == impossible | (1<<i): return 0
        else:  return 1
    
    if impossible not in dp[i].keys():
        if impossible == impossible | (1<<i):
            dp[i][impossible] = dfs(i+1, impossible )
        else:
            nextImpossible = impossible | bitmask[i]
            dp[i][impossible] = max( dfs(i+1, nextImpossible) + 1, dfs(i+1, impossible) )
    return dp[i][impossible]
#########################################3
N = int(input())
table = [ [] for i in range(N) ]

whitePos = []
blackPos = []
for i in range(N):
    table[i] = list(map(int, input().split())) 
    for j in range(N):
        if table[i][j] == 1:
            if getColor(N,i,j):
                blackPos.append( [i,j] )
            else:
                whitePos.append( [i,j] )
                
mx = [-1, -1, +1, +1]
my = [-1, +1, -1, +1]
pos, bitmask = whitePos, getImpossibleBitMask( whitePos )
dp = [ {} for i in range(len(whitePos)) ] 
result = dfs( 0, 0 )

pos, bitmask = blackPos, getImpossibleBitMask( blackPos )
dp = [ {} for i in range(len(blackPos)) ] 
result += dfs( 0, 0 )

print( result )