# 15683번: 감시
import copy

def sol( cctvNumber, table, checkNum ):
    global result, N, M, blockNum
    if cctvNumber == len(cctvPos):
        result = min( result, blockNum-checkNum )
    else:
        i, j, cctvVer = cctvPos[cctvNumber]
        
        # cctv version에 따라 움직일 수 있는 option list 정보를 가져옴
        moveOption = moveOptions[cctvVer]
        
        # option list에서 각 option을 순회
        for option in moveOption:
            copyTable = copy.deepcopy( table )
            copyCheckNum = checkNum
            
            # 하나의 option의 방향에 따라 순회
            for z in option:
                c = 1
                while True:
                    ii, jj = i+mx[z]*c, j+my[z]*c
                    if 0<=ii<N and 0<=jj<M and copyTable[ii][jj]!=6:
                        c+=1
                        if copyTable[ii][jj]==0:
                            copyTable[ii][jj] = 10 + cctvNumber
                            copyCheckNum += 1
                    else:
                        break
            
            # 하나의 option을 모두 수행하였다면 다음 cctv 호출
            sol( cctvNumber+1, copyTable, copyCheckNum )
            
########################################################

N, M = list(map(int, input().split()))
table = [ list(map(int, input().split())) for i in range(N) ]

blockNum = 0
cctvPos = [ ]
for i in range(N):
    for j in range(M):
        if table[i][j] == 0: blockNum += 1
        elif table[i][j] != 6:
            cctvPos.append( [i,j, table[i][j]] )
            
result = blockNum
mx, my = [ -1,1,0,0 ], [0,0,-1,1] # 위 / 아래 / 왼 / 오
moveOptions = [ [], [ [0],[1],[2],[3] ], # 1번 카메라는 위/아래/왼/오 하나만을 선택
              [ [0,1], [2,3] ], # 2번 카메라는 수평/수직 방향을 선택
              [ [0,2], [0,3], [1,2], [1,3] ], # 3번 카메라는 수직방향으로 선택
              [ [0,1,2], [0,1,3], [0,2,3], [1,2,3] ], # 4번 카메라는 아무런 3방향
              [ [0,1,2,3] ] ] # 5번 카메라는 전 방향에 대해 수행

sol( 0, table, 0 )

print( result )