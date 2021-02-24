# 2285번: 우체국
N = int(input())
datas = [list(map(int, input().split())) for i in range(N)]
datas = sorted(datas)

start = result = data[0][0]
leftWeight, rightWeight, totalLen = 0, 0, 0
for x, a in datas[1:]:
    rightWeight += a
    totalLen += (x - start) * a

for index in range(1, N):
    nextLeftWeight = leftWeight + datas[index-1][1]
    nextRightWeight = rightWeight - datas[index][1]
    nextTotalLen = totalLen - rightWeight + nextLeftWeight
    
    if totalLen > nextTotalLen:
        result = data[index][0]
    leftWeight, rightWeight, otalLen = nextLeftWeight, nextRightWeight, nextTotalLen
print( result )