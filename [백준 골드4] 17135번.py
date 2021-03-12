# 17135번: 캐슬 디펜스
from itertools import combinations
import copy

def simulation( p1, p2, p3 ):
    global N, M, D
    tmpTable = copy.deepcopy( table )
    kill = 0
    
    for sec in range(N):
        # 가까운 거 하나씩 타겟팅
        killPos = []
        
        findFlag = [ False, False, False ]
        for d in range( D ):
            for wi, wj in shoot[d]:
                ki, kj = p1[0]+wi, p1[1]+wj
                if findFlag[0]==False and 0<=ki<N and 0<=kj<M and tmpTable[ki][kj]==1 :
                    findFlag[0]=True
                    killPos.append( [ki,kj] )
                
                ki, kj = p2[0]+wi, p2[1]+wj
                if findFlag[1]==False and 0<=ki<N and 0<=kj<M and tmpTable[ki][kj]==1 :
                    findFlag[1]=True
                    killPos.append( [ki,kj] )
                
                ki, kj = p3[0]+wi, p3[1]+wj
                if findFlag[2]==False and 0<=ki<N and 0<=kj<M and tmpTable[ki][kj]==1 :
                    findFlag[2]=True
                    killPos.append( [ki,kj] )
                
                if len(killPos)==3: break
            if len(killPos)==3: break
        
        # 죽이기
        for ki, kj in killPos:
            if tmpTable[ki][kj]==1:
                tmpTable[ki][kj]=0
                kill += 1
    
        # 좀비 1칸 앞으로
        for n in range(N-2,-1,-1):
            for m in range(M):
                tmpTable[n+1][m] = tmpTable[n][m]
                tmpTable[n][m] = 0
        
    return kill
##################################################################
N, M, D = list(map(int, input().split()))
table = [ list(map(int, input().split())) for i in range(N) ]

shoot = [ [] for i in range(D) ]
shoot[0]=[[-1,0]]
for d in range(1,D):
    for left in range( -d, d+1, 1 ):
        shoot[d].append( [ -(d+1-abs(left)) , left] )
    
result = 0
for p1, p2, p3 in list( combinations( [i for i in range(M)], 3 ) ):
    result = max( result, simulation( [N, p1], [N, p2], [N, p3] ) )
    
print( result )