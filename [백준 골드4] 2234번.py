# 2234번: 성곽
from collections import deque

def decoding( wallN ):
    result = ""
    while wallN > 1:
        result = str(wallN % 2) + result
        wallN //= 2
    result = str(wallN % 2) + result
    return result.zfill(4)

def getRoomSize( i, j, roomNum ):
    global n, m
    table[i][j] = roomNum
    roomSize = 1
    queue = deque()
    queue.append( [i,j] )
    while queue:
        i,j = queue.popleft()
        
        for z in range(4):
            if wallMap[i][j][z] == '0':
                # 벽 코드가 0 여야 이동가능
                mi = i + mx[z]
                mj = j + my[z]
                if 0<=mi<m and 0<=mj<n and table[mi][mj]==0:
                    table[mi][mj]=roomNum
                    roomSize+=1
                    queue.append( [mi,mj] )
    return roomSize
#############################################################
# input decoding
n, m = list(map(int, input().split()))
wallMap = [ list(map(int, input().split())) for i in range(m) ]
for i in range(m):
    for j in range(n):
        wallMap[i][j] = decoding( wallMap[i][j] )
# wall code : '남동북서' -> [아래, 오른쪽, 위쪽, 왼쪽] -> [ [1,0], [0,1], [-1,0], [0,-1] ]
mx = [1, 0, -1, 0]
my = [0, 1, 0, -1]        

# make room Table
table = [ [0 for i in range(n)] for i in range(m) ]
sizes = [0]
roomNum = 1
for i in range(m):
    for j in range(n):
        if table[i][j] == 0:
            size = getRoomSize( i, j, roomNum )
            sizes.append( size )
            roomNum += 1

# find big size room
result = sizes[0]
for i in range(m):
    for j in range(n):
        if i+1<m and table[i][j]!=table[i+1][j]: # 아래의 있는 방과 방번호가 다른 경우
            roomNum1, roomNum2 = table[i][j], table[i+1][j]
            result = max( result, sizes[roomNum1]+sizes[roomNum2] )
        if j+1<n and table[i][j]!=table[i][j+1]: # 오른쪽의 있는 방과 방번호가 다른 경우
            roomNum1, roomNum2 = table[i][j], table[i][j+1]
            result = max( result, sizes[roomNum1]+sizes[roomNum2] )
            
# 1. 이 성에 있는 방의 개수
print( roomNum-1 ) 
# 2. 가장 넓은 방의 넓이
print( max(sizes) )
# 3. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
print( result )