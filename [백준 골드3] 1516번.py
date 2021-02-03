# 1516번: 게임 개발
import heapq

N = int(input())
datas = [ [] for i in range(N+1) ]
beforNum = [ 0 for i in range(N+1) ]
cost = [ 0 for i in range(N+1) ]

for i in range(1, N+1):
    data = list(map(int, input().split()))
    
    for befor in data[1:-1]: datas[befor].append( i )
    beforNum[i] = len(data)-2
    cost[i] = data[0]
    
heap = []
for i in range(1, N+1):
    if beforNum[i] == 0: # 선행건물이 없는 건물
        heapq.heappush( heap, [cost[i], i] ) # 끝나는 시간 / index
        
result = [ 0 for i in range(N+1) ]
while heap:
    finishTime, index = heapq.heappop( heap )
    result[index] = finishTime
    
    for after in datas[index]:
        beforNum[after] -= 1
        if beforNum[after] == 0: # 선행 건물이 모두 지어졌다면
            heapq.heappush( heap, [finishTime + cost[after], after] )
    
for r in result[1:]:
    print( r )