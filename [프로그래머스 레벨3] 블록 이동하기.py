# 2020 카카오 공채: 블록 이동하기
from collections import deque

def solution(board):
    answer = 0
    N = len(board)
    
    target = [N-1, N-1]
    tail, head = [0,0], [0,1]
    
    robot = deque( )
    robot.append( [tail, head, 0] )
    
    visited = [ [ [0,0] for i in range(N) ]  for i in range(N) ] # 꼬리기준 가로 / 세로
    visited[0][0][0] = 1
    
    mx = [-1,1,0,0]
    my = [0,0,-1,1]
    while robot:
        tail, head, c = robot.popleft()
        
        if tail == target or head == target:
            return c
        
        for z in range(4): # 좌/우/위/아래 테스트
            newTail = [ tail[0]+mx[z], tail[1]+my[z] ]
            newHead = [ head[0]+mx[z], head[1]+my[z] ]
            
            if 0<=newTail[0]<N and 0<=newTail[1]<N and 0<=newHead[0]<N and 0<=newHead[1]<N \
            and board[newTail[0]][newTail[1]]==0 and board[newHead[0]][newHead[1]]==0:
                if newTail[0]==newHead[0] and visited[newTail[0]][newTail[1]][0]==0:
                    visited[newTail[0]][newTail[1]][0]= 1
                    robot.append( [newTail, newHead, c+1] )
                elif newTail[1]==newHead[1] and visited[newTail[0]][newTail[1]][1]==0:
                    visited[newTail[0]][newTail[1]][1]= 1
                    robot.append( [newTail, newHead, c+1] )

        # Roate
        if tail[0] == head[0]: # 가로 모드
            # Head기준 시계방향
            if head[0] >= 1 and board[head[0]-1][head[1]-1]==0 and board[head[0]-1][head[1]]==0:
                newTail = [ head[0]-1, head[1] ]
                if visited[ newTail[0] ][ newTail[1] ][1] == 0:
                    visited[ newTail[0] ][ newTail[1] ][1] = 1
                    robot.append( [ newTail, head, c+1 ] )
            
            # Head기준 반 시계방향
            if head[0] < N-1 and board[head[0]+1][head[1]-1]==0 and board[head[0]+1][head[1]]==0:
                newhead = [ head[0]+1, head[1] ]
                if visited[ head[0] ][ head[1] ][1] == 0:
                    visited[ head[0] ][ head[1] ][1] = 1
                    robot.append( [ head, newhead, c+1 ] )
            
            # Tail기준 시계방향
            if tail[0] < N-1 and board[tail[0]+1][tail[1]+1]==0 and board[tail[0]+1][tail[1]]==0:
                newhead = [ tail[0]+1, tail[1] ]
                if visited[ tail[0] ][ tail[1] ][1] == 0:
                    visited[ tail[0] ][ tail[1] ][1] = 1
                    robot.append( [ tail, newhead, c+1 ] )
            
            # Tail기준 반 시계방향
            if tail[0] >= 1 and board[tail[0]-1][tail[1]+1]==0 and board[tail[0]-1][tail[1]]==0:
                newTail = [ tail[0]-1, tail[1] ]
                if visited[ newTail[0] ][ newTail[1] ][1] == 0:
                    visited[ newTail[0] ][ newTail[1] ][1] = 1
                    robot.append( [ newTail, tail, c+1 ] )
            
            
        else: # 세로모양으로 존재
            # Head기준 시계방향
            if head[1] < N-1 and board[head[0]-1][head[1]+1]==0 and board[head[0]][head[1]+1]==0:
                newHead = [ head[0], head[1]+1 ]
                if visited[ head[0] ][ head[1] ][0] == 0:
                    visited[ head[0] ][ head[1] ][0] = 1
                    robot.append( [ head, newHead, c+1 ] )
            
            # Head기준 반 시계방향
            if head[1] >= 1 and board[head[0]-1][head[1]-1]==0 and board[head[0]][head[1]-1]==0:
                newTail = [head[0], head[1]-1]
                if visited[ newTail[0] ][ newTail[1] ][0] == 0:
                    visited[ newTail[0] ][ newTail[1] ][0] = 1
                    robot.append( [ newTail, head, c+1 ] )
            
            # Tail기준 시계방향
            if tail[1] >= 1 and board[tail[0]+1][tail[1]-1]==0 and board[tail[0]][tail[1]-1]==0:
                newTail = [ tail[0], tail[1]-1 ]
                if visited[ newTail[0] ][ newTail[1] ][0] == 0:
                    visited[ newTail[0] ][ newTail[1] ][0] = 1
                    robot.append( [ newTail, tail, c+1 ] )
            
            # Tail기준 반 시계방향
            if tail[1] < N-1 and board[tail[0]+1][tail[1]+1]==0 and board[tail[0]][tail[1]+1]==0:
                newHead = [tail[0], tail[1]+1]
                if visited[ tail[0] ][ tail[1] ][0] == 0:
                    visited[ tail[0] ][ tail[1] ][0] = 1
                    robot.append( [ tail, newHead, c+1 ] )
            
    
    return answer