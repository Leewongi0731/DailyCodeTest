# 16724번: 피리 부는 사나이
N, M = list(map(int, input().split()))
graph = [ list(input()) for i in range(N) ]

check = [ [0]*M for i in range(N) ]
checkNum = 1
count = 0

move = { 'U':[-1,0], 'D':[1,0], 'L':[0,-1], 'R':[0,1] }

for i in range(N):
    for j in range(M):
        if check[i][j] != 0:
            continue
        
        ii, jj = i, j
        check[ii][jj] = checkNum
        increaseBit = True
        while True:            
            x, y = move[ graph[ii][jj] ]
            mi, mj = ii+x, jj+y
            
            if mi < 0 or mi >= N or mj < 0 or mj >= M:
                break
            
            if check[mi][mj] == 0: # add
                check[mi][mj] = checkNum
                ii, jj = mi, mj
            elif check[mi][mj] < checkNum: # 이전에 추가된 곳 -> 합침
                increaseBit = False
                break
            elif check[mi][mj] == checkNum: # 반복구간 발견
                break
        
        checkNum += 1
        if increaseBit:
            count += 1

print( count )