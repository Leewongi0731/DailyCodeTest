# 1005번: ACM Craft
import sys
import heapq

T = int(input())
for _ in range(T):
    N, K = list(map(int, input().split())) # 첫째 줄에 건물의 개수 N 과 건물간의 건설순서규칙의 총 개수 K이 주어진다
    D = [0] + list(map(int, input().split())) # 둘째 줄에는 각 건물당 건설에 걸리는 시간 D가 공백을 사이로 주어진다
    
    graph = [ [0 for j in range(N+1)] for i in range(N+1)]
    count = [ 0 for i in range(0, N+1) ]
    for i in range(K): # 셋째 줄부터 K+2줄까지 건설순서 X Y가 주어진다. 건물 X를 지은 다음에 건물 Y를 짓는 것이 가능
        X, Y = list(map(int, input().split()))
        graph[ X ][ Y ] = 1
        count[ Y ] += 1

    W = int(input())  # target

    useNum = [ 0 for i in range(0, N+1) ]
    tmpList = [W]
    while tmpList:
        tmp = tmpList.pop()
        if useNum[ tmp ] == 0:
            useNum[ tmp ] = 1
            tmpList += [ i for i in range(1, N+1) if graph[ i ][ tmp ] == 1 ]
    
    for i in range(1, N+1):
        if useNum[ i ] != 1: # not use
            count[i] = 10000000
    
    ready = [ [D[i], i] for i in range(1, N+1) if count[i] == 0 ]
    heap = []
    for time, index in ready:
        heapq.heappush( heap, ( time, index ) ) # endTime, index
    
    result = 0
    while True:
        time, index = heapq.heappop(heap)
        result = time
        
        if index == W:
            break
        
        findW = False
        for nextIndex in [ i for i in range(1, N+1) if graph[ index ][ i ] == 1 ]:
            count[ nextIndex ] -= 1
            if count[ nextIndex ] == 0:
                if nextIndex == W:
                    findW = True
                    result = result + D[nextIndex]
                    break
                
                heapq.heappush( heap, ( result + D[nextIndex], nextIndex ) ) # endTime, index
                
        if findW == True:
            break
    print(result)