# 2539번: 모자이크
# 행의 개수와 열의 개수
H, W = list(map(int, input().split()))
# 색종이 갯수 사용할 색종이는 100장 이하
N = int(input())
# 잘못 칠해진 위치
M = int(input())
datas = set()
minV = 0
for i in range(M):
    h, w = list(map(int, input().split()))
    minV = max( minV, h ) # 높이 정보는 최소의 사각형 높이를 측정할 때만 사용
    datas.add( w )
datas = sorted(  list(datas) ) # 가로위치를 정렬

left, right = minV, H
while left <= right:
    # 기대 값
    mid = (left+right) // 2
    
    paperCount = 0
    lastPaper = 0
    for data in datas:
        if data > lastPaper:
            paperCount += 1
            lastPaper = data + mid - 1
            if lastPaper >= W: break # 모든 범위 가능
            if paperCount > N:break # 허용 종이 갯수 초과
    
    # 현재 기대 값으로는 N개 이하로 붙힐 수 없음 -> left을 올려 mid(기대값)을 증가시킴
    if paperCount > N:
        left = mid+1
        
    # 현재 기대 값으로도 N개 이하로 붙힐 수 있음 -> right을 줄여 더 최적의 mid값을 찾음
    else:
        right = mid-1
        result = mid
        
print( result )