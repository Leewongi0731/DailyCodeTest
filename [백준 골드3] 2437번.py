# 2437번: 저울
# 아이디어 : data를 정렬한 후, 해당 data차례일때는 추가하여 만들 수 있는 경우가 [ data+1, data+maxValue ] 임을 이용
# 새로 만들 수 있는 데이터 중, 최소값은 data + 1이지만, 현재의 maxVlaue보다 크다면 그 중간에 못만드는 수가 생김.
N = int(input())
datas = list(map(int,input().split()))
datas = sorted( datas )

maxValue = 0
for data in datas:
    if data-1 > maxValue: break
    else: maxValue += data
print( maxValue + 1 )