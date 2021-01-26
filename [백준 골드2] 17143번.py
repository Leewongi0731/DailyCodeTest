# 17143번: 낚시왕
import heapq

R, C, M = list( map(int, input().split()) )
graph = [ [ [] for i in range(C)] for i in range(R) ]
for _ in range(M):
    r, c, s, d, z = list( map(int, input().split()) )
    if d in [1,2]: s %= 2*(R-1) # ex) R이 5인데, 속도가 20으로 우측으로 이동한다면, 우측으로 초당 4로 이동하는 것과 같음 
    if d in [3,4]: s %= 2*(C-1)
    graph[r-1][c-1] = [ z, d, s ]

mx = [0,-1,1,0,0]
my = [0,0,0,1,-1]
changeDir = [0, 2, 1, 4, 3 ]

result = 0
for human in range(C):
    # 이동
    # 상어 잡기
    for r in range(R):
        if graph[r][human] != []:
            result += graph[r][human][0]
            graph[r][human] = []
            break
            
    # 상어 이동
    sharks = []
    for i in range(R):
        for j in range(C):
            if graph[i][j] != []: # 이동전
                z, d, s = graph[i][j]
                r, c = i, j
                for t in range(s):
                    mr = r + mx[ d ]
                    mc = c + my[ d ]
                    
                    if mr >= 0 and mr < R and  mc >= 0 and mc < C:
                        r, c = mr, mc
                        continue
                    else: # turn
                        d = changeDir[d]
                        r = mr + 2 * mx[d]
                        c = mc + 2 * my[d]
                    
                heapq.heappush( sharks, [ -z, d, s, r, c ] ) # MAX HEAP
    
    # graph Update
    graph = [ [ [] for i in range(C)] for i in range(R) ]
    while sharks:
        z, d, s, r, c = heapq.heappop( sharks )
        if graph[r][c] == []:
            graph[r][c] = [-z, d, s]

print( result )