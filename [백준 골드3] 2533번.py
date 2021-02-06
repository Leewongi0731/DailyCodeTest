# 2533번: 사회망 서비스(SNS)
import sys
sys.setrecursionlimit(10**9) 

def getChildList(cur):
    visited[cur] = True
    for i in link[cur]:
        if not visited[i]:
            child[cur].append(i)
            getChildList(i)
            
def sol( node, isEarlyadopter ):
    if isEarlyadopter: #  해당 Node가 earlyadopter라면
        if dp[ node ][ True ] == -1:
            result = 1 # 자신이 earlyadopter임으로 1로 시작
            for childNode in child[node]:                    
                if len( child[childNode] ) == 0 : result += 0 # child가 leaf노드
                else: result += min( sol(childNode, True), sol(childNode, False) )
            dp[ node ][ True ] = result
        return dp[ node ][ True ]
    
    else: # 해당 Node가 earlyadopter가 아니라면
        if dp[ node ][ False ] == -1:
            result = 0
            for childNode in child[node]:
                if len( child[childNode] ) == 0 : result += 1 # child가 leaf노드
                else: result += sol(childNode, True) # 자기가 earlyadopter가 아님으로, child node가 모두 earlyadopter여야함.
            dp[ node ][ False ] = result
        return dp[ node ][ False ]
###############################################################################################################
N = int(input())
link = [ [] for i in range(N) ]
for _ in range(N-1):
    u, v = list(map(int, sys.stdin.readline().split()))
    link[u-1].append( v-1 )
    link[v-1].append( u-1 )

child = [[] for i in range(N)]
visited = [False] * (N)
getChildList( 0 )

del link, visited
dp = [ [-1,-1] for i in range(N) ]
result = min( sol(0, True), sol(0, False) )
print( result )