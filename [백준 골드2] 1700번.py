# 1700번: 멀티탭 스케줄링
from collections import deque

N, K = list(map(int, input().split()))
datas = list(map(int, input().split()))
dataIndex = [ deque() for i in range(K+1) ]
for i, data in enumerate(datas):
    dataIndex[ data ].append( i )
    
index = 0
plugOn = [ False for i in range(K+1) ]
plugCount = 0
result = 0
while index < K:
    data = datas[index]
    
    if plugOn[ data ] == False:
        if plugCount < N: # 단순 on
            plugOn[ data ] = True
            plugCount += 1
        else: # 빼고 꽃아야 함 : 꽃혀있는 플러그 중, 이젠 사용하지 않거나 가장 오랜 뒤에 사용 할 플러그 제거
            deleteNum = 0
            deleteLen = 0
            for i in range( 1, K+1 ):
                if plugOn[ i ] == True:
                    if len( dataIndex[ i ]  ) == 0:
                        deleteNum = i
                        break
                    elif deleteLen < dataIndex[ i ][0]:
                        deleteLen = dataIndex[ i ][0]
                        deleteNum = i
                        
            plugOn[ deleteNum ] = False
            plugOn[ data ] = True
            result += 1
            
    dataIndex[ data ].popleft()
    index += 1
print( result )