# 2229번: 조 짜기
N = int(input())
datas = list(map(int, input().split()))

dp = [0 for i in range(N)]
minV = maxV = datas[0]
minIndex = maxIndex = 0

for index in range(1, N):
    data = datas[index]
    # 이전 구간의 최대 점수
    beforGroupVal = 0
    
    if data < minV: # 최소 값 변경
        # 이전 범위 최대 값을 더해줌
        if maxIndex != 0:  beforGroupVal = dp[maxIndex-1] 
        minV = data
        minIndex = index
        
    elif data > maxV: # 최대 값 변경
        # 이전 범위 최대 값을 더해줌
        if minIndex != 0: beforGroupVal = dp[minIndex-1]
        maxV = data
        maxIndex = index
        
    else:
        # 새로운 범위 시작
        v1 = dp[index-1]
        flag = False
        
        if minIndex < maxIndex:
            # 새로운 min이 될 수 있나
            beforGroupVal = dp[maxIndex-1]
            if beforGroupVal + maxV - data > v1:
                minV = data
                minIndex = index
                flag = True
                
        elif minIndex > maxIndex:
            # 새로운 max가 될 수 있나
            beforGroupVal = dp[minIndex-1] 
            if beforGroupVal + data - minV > v1:
                maxV = data
                maxIndex = index
                flag = True
            
        if flag == False:
            minV = maxV = data
            minIndex = maxIndex = index
            beforGroupVal = v1
            
    # 해당 구간의 잘 짜여진 정도
    dp[index] = beforGroupVal + maxV - minV
    
print( dp[-1] )