# 2110번: 공유기 설치
N, C = list(map(int, input().split()))
datas = [ int(input()) for i in range(N) ]
datas = sorted( datas )

left = 1 # 최소거리
right = datas[-1] - datas[0] # 최대거리
result = 0
while left <= right:
    mid = (left+right)//2 # 기대거리
    start = datas[0] # 0번 index의 data는 항상 사용
    count = 1 # 0번 index를 사용하기 때문에 count의 시작값은 1
    
    for i in range( 1, N ):
        length = datas[i] - start
        if length >= mid:
            count += 1
            start = datas[i]
            if count >= C: break
        
    if count>=C:
        # 해당 left(최소거리) / right(최대거리)에서 mid(기대거리)의 갯수가 C이상 나온다면,
        # left(최소거리)를 줄여 더 큰 mid(기대거리)에 대해 check함 
        result = mid
        left = mid + 1
    else:
        # 해당 left(최소거리) / right(최대거리)에서 mid(기대거리)의 갯수가 C이상 나오지 않는다면,
        # right(최대거리)를 줄여 더 작은 mid(기대거리)에 대해 check함
        right = mid - 1
print( result )