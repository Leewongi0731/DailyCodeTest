# 16964번: DFS 스페셜 저지
from collections import deque
from bisect import bisect_left

def isPossible( query ):
    global N
    if query[0] != 1: return 0
    
    stack = deque()
    stack.append( query[0] )
    nextIndex = 1
    while stack:
        top = stack[-1]
        
        target = query[nextIndex]
        
        index = bisect_left( graph[top], target )
        if index != len(graph[top]) and graph[top][index] == target:
            stack.append( target )
            nextIndex += 1
            if nextIndex == N: return 1
        else:
            stack.pop()
        
    return 0
##############################
    
N = int(input())
graph = [ [] for i in range(N+1) ]
for i in range(N-1):
    n1, n2 = list(map(int, input().split()))
    graph[n1].append( n2 )
    graph[n2].append( n1 )
    
# 탐색 속도를 높이기 위해 이진탐색 이용
for i in range(1, N+1):
    graph[i] = sorted( graph[i] )
    
    
query = list(map(int, input().split()))
result = isPossible( query )
print(result)