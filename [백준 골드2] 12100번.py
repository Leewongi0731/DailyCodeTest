# 12100번: 2048 (Easy)
import copy
from collections import deque
def move( board, count ):
    global result, N
    topBoard = copy.deepcopy( board )
    underBoard = copy.deepcopy( board )
    leftBoard = copy.deepcopy( board )
    rightBoard = copy.deepcopy( board )
    count += 1
    
    # move Top
    for j in range( 0, N ):
        befor = [0, -1, j, False]
        for i in range( 0, N ):
            if topBoard[i][j] == 0:
                continue
            
            bi,bj = befor[1], befor[2]
            if topBoard[ i ][ j ] == befor[0] and befor[3] == False: # sum
                topBoard[bi][bj] = befor[0] + topBoard[i][j]
                if result < topBoard[bi][bj]: result = topBoard[bi][bj]
                befor[0] = topBoard[bi][bj]
                befor[3] = True
                topBoard[i][j] = 0
            else: # no Sum
                topBoard[bi+1][bj] = topBoard[i][j]
                befor = [ topBoard[i][j], bi+1, bj, False ]
                if bi+1 != i: topBoard[i][j] = 0
    
    # move under
    for j in range( 0, N ):
        befor = [0, N, j, False]
        for i in range( N-1, -1, -1 ):
            if underBoard[i][j] == 0:
                continue
                
            bi,bj = befor[1], befor[2]
            if underBoard[ i ][ j ] == befor[0] and befor[3] == False: # sum
                underBoard[bi][bj] = befor[0] + underBoard[i][j]
                if result < underBoard[bi][bj]: result = underBoard[bi][bj]
                befor[0] = underBoard[bi][bj]
                befor[3] = True
                underBoard[i][j] = 0
            else: # no Sum
                underBoard[bi-1][bj] = underBoard[i][j]
                befor = [ underBoard[i][j], bi-1, bj, False ]
                if bi-1 != i: underBoard[i][j] = 0
            
            
    # move left
    for i in range( 0, N ):
        befor = [0, i, -1, False]
        for j in range( 0, N ):
            if leftBoard[i][j] == 0:
                continue
                
            bi,bj = befor[1], befor[2]
            if leftBoard[ i ][ j ] == befor[0] and befor[3] == False: # sum
                leftBoard[bi][bj] = befor[0] + leftBoard[i][j]
                if result < leftBoard[bi][bj]: result = leftBoard[bi][bj]
                befor[0] = leftBoard[bi][bj]
                befor[3] = True
                leftBoard[i][j] = 0
            else: # no Sum
                leftBoard[bi][bj+1] = leftBoard[i][j]
                befor = [ leftBoard[i][j], bi, bj+1, False ]
                if bj+1 != j: leftBoard[i][j] = 0
            
    # move right
    for i in range( 0, N ):
        befor = [0, i, N, False]
        for j in range( N-1, -1, -1 ):
            if rightBoard[i][j] == 0:
                continue
            
            bi,bj = befor[1], befor[2]
            if rightBoard[ i ][ j ] == befor[0] and befor[3] == False: # sum
                rightBoard[bi][bj] = befor[0] + rightBoard[i][j]
                if result < rightBoard[bi][bj]: result = rightBoard[bi][bj]
                befor[0] = rightBoard[bi][bj]
                befor[3] = True
                rightBoard[i][j] = 0
            else: # no Sum
                rightBoard[bi][bj-1] = rightBoard[i][j]
                befor = [ rightBoard[i][j], bi, bj-1, False ]
                if bj-1 != j: rightBoard[i][j] = 0

    if count <= 4:
        queue.append( ( topBoard, count ) )
        queue.append( ( underBoard, count ) )
        queue.append( ( leftBoard, count ) )
        queue.append( ( rightBoard, count ) )
        
    return result
###########################################
N = int(input())
board = [[] for i in range(N) ]
for i in range(N):
    board[i] = list(map(int, input().split()))

queue = deque()
queue.append( ( copy.deepcopy( board ), 0 ) )
result = max( [ max(board[i]) for i in range(len(board)) ] )
while queue:
    b, c = queue.popleft()
    result = move( b, c )
            
print( result )