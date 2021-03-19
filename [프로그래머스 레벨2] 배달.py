# Summer/Winter Coding: 배달
import heapq

def solution(N, road, K):
    graph = [ {} for i in range(N+1) ]
    for s,e,c in road:
        try:
            graph[s][e] = min( graph[s][e], c )
            graph[e][s] = min( graph[e][s], c )
        except:
            graph[s][e] = c
            graph[e][s] = c
    
    cost = [ 123456789 for i in range( N+1 ) ]
    cost[1] = 0
    queue = [ ]
    heapq.heappush( queue, [1, cost[1]] )
    
    while queue:
        n, c = heapq.heappop(queue)     
        
        if cost[n]!=c:continue
            
        for nextNode, moveCost in graph[n].items():
            if cost[nextNode] > cost[n] + moveCost:
                cost[nextNode] = cost[n] + moveCost
                heapq.heappush( queue, [nextNode, cost[nextNode]] )
            
            
    answer = 0
    for c in cost:
        if c <= K: answer += 1 

    return answer