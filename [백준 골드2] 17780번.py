# 17780번: 새로운 게임
from collections import deque

N, K = list(map(int, input().split()))
table = [ list(map(int, input().split())) for i in range(N) ] # 0은 흰색, 1은 빨간색, 2는 파란색
horses = [ list(map(int, input().split())) for i in range(K) ] # i,j / 1부터 순서대로 →, ←, ↑, ↓

gameTable = [ [ [] for i in range(N) ] for i in range(N) ] # i, j -> numberList
for num, horse in enumerate(horses):
    horses[num][0] -= 1
    horses[num][1] -= 1
    horses[num][2] -= 1
    
    i, j, d = horses[num][0], horses[num][1], horses[num][2]
    gameTable[i][j].append( num )
    
mx, my = [0, 0, -1, 1 ], [1, -1, 0, 0]
mi, mj = 0,0
turnDir = [ 1,0,3,2 ]
turn = 0
while turn <= 1000:
    turn += 1
    
    for num in range(K):
        i, j, d = horses[num][0], horses[num][1], horses[num][2]
        if gameTable[i][j][0] == num: # 해당 위치의 바닥이 해당 hourse인 경우만 게임을 진행
            mi, mj = i+mx[d], j+my[d]
            if 0<=mi<N and 0<=mj<N and table[mi][mj]!=2:
                if table[mi][mj]==0: # 흰색 -> 그대로 쌓음
                    gameTable[mi][mj] += gameTable[i][j]
                else: # 빨강 : 위아래 변경하고 쌓음
                    gameTable[mi][mj] += list( reversed(gameTable[i][j]) )
                
                for beforNum in gameTable[i][j]:    
                    horses[beforNum][0] = mi
                    horses[beforNum][1] = mj
                gameTable[i][j] = []
                
                
            else: # 이동할려는 곳이 경기장 밖 or 파란색
                td = turnDir[d]
                mi, mj = i+mx[td], j+my[td]
                horses[num][2] = td # 방향 변경
                
                if 0<=mi<N and 0<=mj<N and table[mi][mj]!=2: # 반대 방향으로 1칸 이동
                    if table[mi][mj]==0: # 흰색 -> 그대로 쌓음
                        gameTable[mi][mj] += gameTable[i][j]
                    else: # 빨강 : 위아래 변경하고 쌓음
                        gameTable[mi][mj] += list( reversed(gameTable[i][j]) )

                    for beforNum in gameTable[i][j]:    
                        horses[beforNum][0] = mi
                        horses[beforNum][1] = mj
                    gameTable[i][j] = []
                    
                else: # 반대도 그렇다면, 현위치에서 방향만 변경
                    mi, mj = i, j

            if len(gameTable[mi][mj]) >= 4: break
            
        else: # 이동 X
            pass 
        
    if len(gameTable[mi][mj]) >= 4: break

if turn > 1000: print( -1 )
else: print( turn )