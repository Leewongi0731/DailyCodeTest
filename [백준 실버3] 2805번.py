# 2805번: 나무 자르기
# 나무의 수 N, 집으로 가져가려고 하는 나무의 길이 M
N, M = list(map(int, input().split()))
datas = list(map(int, input().split()))
datas = sorted( datas, reverse=True ) # 오른차순 정렬

# 최소 높이, 최대 높이
left, right = 1, 1000000000
result = 0
while left <= right:
    # 절단기 기대 높이
    mid = (left+right)//2
    totalWood = 0
    for data in datas:
        if data < mid: break
        # 절단 후 얻은 나무 양
        totalWood += data-mid
        if totalWood >= M: break
            
    if totalWood >= M:
        # 범위를 mid+1~right로 변경하여 mid(기대 높이)를 늘림
        result = max(result, mid)
        left = mid+1
    else:
        # 범위를 left~mid-1로 변경하여 mid(기대 높이)를 줄임
        right=mid-1
print( result )