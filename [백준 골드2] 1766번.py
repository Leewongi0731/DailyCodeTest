# 1766번 : 문제집 
import heapq

N, M = list(map(int, input().split()))
result = []
check = [ [0, [], []] for i in range(N+1) ]
heap = []
for _ in range(M):
    a, b = list(map(int, input().split()))
    check[a][1].append( b )
    check[b][2].append( a )

for i in range(1, N+1): 
    if check[i][2] == []: 
        check[i][0] = 1
        heapq.heappush( heap, i )

while len(result) != N:
    target = heapq.heappop( heap )
    result.append( target )
    check[ target ][ 0 ] = 2

    for after in check[ target ][ 1 ]:
        if check[after][0] == 0:
            addBit = True
            for befor in check[ after ][ 2 ]:
                if check[befor][0] != 2:
                    addBit =False
                    break
            if addBit:
                check[after][0] = 1
                heapq.heappush( heap, after )

print( ' '.join(map(str, result)) )    