# 3190번: 뱀
from collections import deque
N = int(input())
K = int(input())

graph = [ [0 for i in range(N)] for j in range(N) ]
for _ in range(K):
    i, j = list(map(int, input().split()))
    graph[i-1][j-1] = 1

L = int(input())
events = [ [] for i in range(L)]
for i in range(L):
    x, c = input().split()
    x = int(x)
    events[ i ] = [x, c]
eventIndex = 0

mx = [-1,1,0,0]
my = [0,0,-1,1]
changeL = [ 2, 3, 1, 0 ]
changeD = [ 3, 2, 0, 1 ]
sec = 0
snake = deque()
snake.append( [0,0] )
nowDire = 3 # 시작은 0,0 에서 오른쪽 방향

while True:
    if eventIndex < L and events[ eventIndex ][ 0 ] == sec:
        if events[ eventIndex ][ 1 ] == "L":
            nowDire = changeL[ nowDire ]
        else: 
            nowDire = changeD[ nowDire ]
        eventIndex += 1
        
    sec += 1
    nextHeadPosI = snake[0][0] + mx[nowDire]
    nextHeadPosJ = snake[0][1] + my[nowDire]
    nextPos = [nextHeadPosI, nextHeadPosJ]
    if nextHeadPosI < 0 or nextHeadPosJ < 0 or nextHeadPosI >= N or nextHeadPosJ >= N or nextPos in snake: # 벽 또는 자기몸에 닿음
        break
    
    if graph[ nextHeadPosI ][ nextHeadPosJ ] == 0: # no eat apple
        snake.pop()
    else:
        graph[ nextHeadPosI ][ nextHeadPosJ ] = 0
    snake.appendleft( nextPos )
    
print( sec )