# 20924번: 트리의 기둥과 가지
# 2021 ICPC Sinchon Winter Algorithm Camp Contest - 초급 : D

import sys
from collections import deque

N, R = list(map(int, input().split()))
tree = [ {} for i in range(N+1)]
for _ in range(N-1):
    a, b, d = list(map(int, sys.stdin.readline().split()))
    tree[a][b] = d
    tree[b][a] = d

cost = [ sys.maxsize for i in range(N+1) ]
cost[R] = 0
# 기가 노드 찾기, 기둥 길이 측정
if len(tree[R]) != 1:
    len1 = 0
    giga = R
else: 
    len1 = 0
    giga = None
    node = R
    while True:
        if len( tree[node] ) >= 3:
            giga = node
            break
        findNext = False
        for childNode, dist in tree[node].items():
            if cost[childNode]==sys.maxsize:
                cost[childNode] = cost[node] + dist
                len1 = cost[childNode]
                node = childNode
                findNext = True
                break
                
        if findNext==False: break

            
if giga == None: # 기가노드가 존재하지 않는경우
    len2 = 0
else:
    cost[giga] = 0
    queue = deque()
    queue.append( giga )
    len2 = 0
    while queue:
        node = queue.popleft()
        
        for childNode, dist in tree[node].items():
            if cost[childNode]==sys.maxsize:
                cost[childNode] = cost[node] + dist
                len2 = max( len2, cost[childNode] )
                queue.append( childNode )

print( len1, len2 )