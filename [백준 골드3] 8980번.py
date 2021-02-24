# 8980번: 택배
N, C = list(map(int, input().split())) # 마을 수 / 최대 무게
M = int(input()) # query 갯수
datas = [ list(map(int, input().split())) for i in range(M) ]
datas = sorted( datas, key=lambda x:x[1] )

# 각 마을에 가지고 갈 수 있는 최대 무게
possibleMaxWeight = [ C for i in range(N+1) ]

result = 0
for s, e, w in datas:    
    # 해당 query내의 범위의 마을에서 가지고 갈 수 있는 최대 무게중 최소 값
    # 1->5로 가는 택배 query중, 이전에 3->4 가는 query로 인해 3,4 범위의 최대 무게 값이 변경되었다면
    # 1->5로 가는 택배의 최대값도 영향을 받음
    tmp = min( possibleMaxWeight[ s:e+1 ] )
    
    # query에서 요청한 무게와, 가능한 최대값 중 작은 값을 확정 지음
    tmp = min( tmp, w )
    
    # 해당 무게로 배달을 하기로 하였다면, 해당 구간내에 해당 무게만큼은 더 못 받음
    for i in range( s, e+1 ):
        possibleMaxWeight[i] -= tmp

    result += tmp
    print( s, e, w, possibleMaxWeight, tmp, result )
print( result )