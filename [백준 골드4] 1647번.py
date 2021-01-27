# 1647번: 도시 분할 계획
# PyPy3로 제출하면 메모리초과... 
# Python3로 제출하면 통과

import sys
sys.setrecursionlimit(10**6)

def getParent( i ):
    if parent[i] == i: return i
    else: return getParent( parent[i] )
##############################################################
N, M = list( map(int, input().split()) )
cost = [ list(map(int, sys.stdin.readline().split())) for i in range(M) ]
cost = sorted( cost, key=lambda x : x[2] ) # cost  오름차순 정렬

parent = [ i for i in range(N+1) ]
result = 0
groupNum = N
for a, b, c in cost:
    if groupNum == 2: break # 그룹이 2개 남았다면 중지
        
    aParent = getParent(a)
    bParent = getParent(b)
    
    if aParent == bParent: continue
    
    # 서로 다른 그룹이라면, 연결
    if aParent < bParent:        
        parent[bParent] = parent[a] = parent[b] = aParent
    else:
        parent[aParent] = parent[a] = parent[b] = bParent
        
    groupNum -= 1
    result += c
    
print(result)