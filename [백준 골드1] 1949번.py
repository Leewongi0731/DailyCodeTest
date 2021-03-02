# 1949번: 우수 마을
from collections import deque

N = int(input())
datas = [0] + list(map(int, input().split()))
graph = [ [[],[]] for i in range(N+1) ]
for _ in range(N-1):
    a, b = list(map(int, input().split()))
    graph[a][0].append( b )
    graph[b][0].append( a )

ready = deque()
for i in range(1, N+1):
    if len( graph[i][0] ) == 1: ready.append( i )

dp = [ [0, 0] for i in range(N+1) ]
while ready:
    n = ready.popleft()
    
    # 내가 우수마을이 되기 위해서는 인접한 모든 노드가 우수마을이 되면 안됨
    dp[n][True] = datas[n] + sum([ dp[beforNode][False] for beforNode in graph[n][1] ] )
    
    
    # 내가 우수마을이 아니라면, 이전에 인접한 노드중 하나는 우수마을이여 한다.
    if graph[n][1]==[]: pass
    else:
        tmp = 0
        flag = False
        for beforNode in graph[n][1]:
            if dp[beforNode][False]<=dp[beforNode][True]: flag = True
            tmp += max( dp[beforNode][False], dp[beforNode][True] )
            
        if flag==False:
            minGap, minGapIndex = 1234567890, -1
            for i, beforNode in enumerate(graph[n][1]):
                gap = dp[beforNode][False] - dp[beforNode][True]
                if gap < minGap:
                    minGap = gap
                    minGapIndex = i
            tmp -= dp[minGapIndex][False]
            tmp += dp[minGapIndex][True]
        dp[n][False] = tmp

    for nextNode in graph[n][0]:
        graph[nextNode][0].remove( n )
        graph[nextNode][1].append( n )
        if len( graph[nextNode][0] ) == 1: ready.append( nextNode )
print( max( dp[n][True], dp[n][False] ) )