# 1654번: 랜선 자르기
K, N = list(map(int, input().split()))
datas = [ int(input()) for i in range(K) ]
datas = sorted( datas )

# 랜선의 최소길이, 최대 길이
left = 1
right = 2**31 - 1

result = 0
while left <= right:
    # 랜선 기대 길이
    mid = (left+right)//2
    count = 0 
    
    for data in datas:
        count += data // mid
        if count >= N: break
            
    if count>=N:
        # 범위를 mid+1~right로 변경하여 mid(기대길이)를 늘림
        result = max(result, mid)
        left = mid+1
    else:
        # 범위를 left~mid-1로 변경하여 mid(기대길이)를 줄임
        right=mid-1
print( result )