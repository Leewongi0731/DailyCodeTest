# 3109번: 빵집
from collections import deque

R, C = list(map(int, input().split()))
table = [ list(input()) for i in range(R) ]

visited = [ [False for i in range(C)] for i in range(R) ]
result = 0
for r in range(R):
    if table[r][0] == 'x': continue
    
    stack = deque()
    stack.append( [r,0] )
    successFlag = False
    while stack:
        nowR, c = stack[-1]
        findNext = False
        
        if c==C-1: # 마지막까지 도달하였다면,
            successFlag=True
            break
        
        for w in [-1,0,1]:
            nextR = nowR+w
            if 0<=nextR<R and table[nextR][c+1]=='.' and visited[nextR][c+1]==False:
                visited[nextR][c+1]=True
                findNext = True
                stack.append( [nextR,c+1] )
                break
        
        if findNext==False:
            stack.pop()
    
    if successFlag:
        result+=1
        
print( result )