# 17406번: 배열 돌리기 4
from itertools import permutations
import copy

def roate( centeri, centerj, s ):
    leftTop = [centeri-s, centerj-s ]
    rightTop = [centeri-s, centerj+s ]
    leftBot = [centeri+s, centerj-s ]
    rightBot = [centeri+s, centerj+s ]
    
    leftTopVal = copyTable[ leftTop[0] ][ leftTop[1] ]
    rightTopVal = copyTable[ rightTop[0] ][ rightTop[1] ]
    leftBotVal = copyTable[ leftBot[0] ][ leftBot[1] ]
    rightBotVal = copyTable[ rightBot[0] ][ rightBot[1] ]

    # 위쪽
    i = leftTop[0]
    for j in range( rightTop[1], leftTop[1]+1, -1 ):
        copyTable[i][j] = copyTable[i][j-1]
    
    # 오른쪽
    j = rightBot[1]
    for i in range( rightBot[0], rightTop[0]+1, -1 ):
        copyTable[i][j] = copyTable[i-1][j]
    
    # 아래
    i = leftBot[0]
    for j in range( leftBot[1], rightBot[1]-1 ):
        copyTable[i][j] = copyTable[i][j+1]
        
    # 왼쪽
    j = leftTop[1]
    for i in range( leftTop[0], leftBot[0]-1 ):
        copyTable[i][j] = copyTable[i+1][j]
    
    copyTable[ leftTop[0] ][ leftTop[1]+1 ] = leftTopVal
    copyTable[ rightTop[0]+1 ][ rightBot[1] ] = rightTopVal
    copyTable[ leftBot[0]-1 ][ leftBot[1] ] = leftBotVal
    copyTable[ rightBot[0] ][ rightBot[1]-1 ] = rightBotVal

#######################################################
    
N, M, K = list(map(int, input().split()))
table = [ list( map(int, input().split()) ) for i in range(N)]
op = [ list(map(int, input().split())) for i in range(K) ]
result = 10000000000000000
for o in list(permutations( op, K)): # 임의의 operation 순서를 만들고, 가장작은 tableValue를 구함
    copyTable = copy.deepcopy( table )
    for r, c, s in o:
        centeri, centerj = r-1, c-1
        for s_ in range(1, s+1):  roate( centeri, centerj, s_ )
    tmp = min([ sum(row) for row in copyTable ])
    result = min ( result, tmp )
print( result )