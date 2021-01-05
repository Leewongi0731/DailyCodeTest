# 2056번: 작업
import heapq
N = int(input())

firstJob = { i:[] for i in range(N) }
count = [ 0 for i in range(N) ]
time = [0 for i in range(N)]

heap = []
for i in range( N ):
    data = list( map(int, input().split()) )
    time[ i ] = data[0]
    count[ i ] = data[1]
    if data[1] != 0:
        for beginNum in data[2:]:
            firstJob[ beginNum-1 ].append( i )
    else:
        heapq.heappush( heap, ( time[i], i ) ) # endTime, index
        

result = 0
passCount = 0
while passCount < N:
    tmp = heapq.heappop(heap)
    passCount += 1
    result = tmp[0] # time -> endTime
    for f in firstJob[ tmp[1] ]:
        count[f] -= 1
        if count[f] == 0:
            heapq.heappush( heap, ( result + time[f], f ) ) # endTime, index
    
print( result )