# 1197번: 최소 스패닝 트리
V, E = list(map(int, input().split()))
MAX = 100000000

graph = { i : {} for i in range(V) }
for _ in range(E):
    A, B, C = list(map(int, input().split()))
    graph[ A-1 ][ B-1 ] = C
    graph[ B-1 ][ A-1 ] = C

visted = [ 0 for i in range(V) ]
visted[0] = 1
ready = graph[0]
count = 1
result = 0

while count < V:
    minCost = MAX
    targetIndex = 0
    for i in ready.keys(): # 가장 작은 cost 찾기
        if minCost > ready[ i ]:
            minCost = ready[ i ]
            targetIndex = i
    
    visted[ targetIndex ] = 1
    ready.pop( targetIndex )
    count += 1
    result += minCost
    
    for i in graph[targetIndex].keys(): # update
        if visted[i] == 1:
            continue
        
        cost = graph[targetIndex][i]
        try:
            if ready[i] > cost:
                ready[i] = cost
        except: # 추가
            ready[i] = cost

print( result )