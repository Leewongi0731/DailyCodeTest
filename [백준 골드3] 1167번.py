# 1167번: 트리의 지름
import sys

def DFS( N, start, visited ):
    for nextNode, moveCost in graph[start].items():
        if visited[ nextNode ]==-1:
            visited[ nextNode ]=visited[start]+moveCost
            DFS( N, nextNode, visited )
            
##############################################################################    

N = int(input())
graph = [ {} for i in range(N+1) ]
for i in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    node = data[0]
    for dataIndex in range( 1, len(data)-1, 2 ):
        linkNode = data[dataIndex]
        graph[node][ linkNode ] = data[dataIndex+1]

# 아이디어 : 임의 점에서 가장 먼 노드는, 트리 지름의 한 축이다.
visited = [ -1 for i in range(N+1) ]
visited[1] = 0
DFS(N, 1, visited)

# 트리지름의 한 지점 찾기
longest = 0
edgeNode = 0
for i in range(2, N+1):
    if longest < visited[i]:
        longest = visited[i]
        edgeNode = i

# 트리지름에서 DFS를 수행해서 나온 가장 먼 노드와의 거리가 트리의 지름이다.
visited = [ -1 for i in range(N+1) ]
visited[edgeNode] = 0
DFS(N, edgeNode, visited)

print( max(visited) )



'''
# 기존에 통과되었던 Dp를 이용한 방법 : 재채점으로 시간초과 결과를 받음
# DFS, Tree Dp 이용
# 2≤V≤100,000의 범위임으로, V*V 배열은 생성 할 수 없으므로, list, dict으로 dp구현
from collections import deque
import sys

def DFS( node ):
    stack = [ [0, node] ] # beforNode, nowNode
    dp[0][node] = 0
    
    while stack:
        beforNode, node = stack[-1]
        findNext = False
        for nextNode, moveCost in graph[node].items():
            if nextNode != beforNode:
                if nextNode not in dp[node].keys():
                    dp[node][nextNode] = moveCost
                    stack.append( [node, nextNode] )
                    findNext = True
                    break
        
        if findNext==False:
            nextCost = [ dp[node][nextNode] for nextNode, moveCost in graph[node].items() if nextNode != beforNode ]
            if nextCost != []: dp[beforNode][node] += max(nextCost)
            stack.pop()
    
##############################################################################    

N = int(input())
graph = [ {} for i in range(N+1) ]
for i in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    node = data[0]
    for dataIndex in range( 1, len(data)-1, 2 ):
        linkNode = data[dataIndex]
        graph[node][ linkNode ] = data[dataIndex+1]
        
dp = [ {} for i in range(N+1) ]
result = 0
for node in range(1, N+1):
    DFS(node)
    result = max( result, dp[0][node] )
print( result )
'''