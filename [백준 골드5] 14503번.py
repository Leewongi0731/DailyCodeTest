# 14503번: 로봇 청소기
N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(N)]

from collections import deque

result = 0
q = deque( )
q.append( [r,c,d] )
# 북, 남, 서, 동
mx = [-1,1,0,0]
my = [0,0,-1,1]
left = [ 2, 0, 3, 1 ]
back = [ 1, 2, 0, 3 ]
rotate = [ 3, 0, 1, 2 ]

while q:
    r,c,d = q.popleft()
    graph[r][c] = 2 # clean
    
    backFlag = True
    nr, nc = r, c
    for _ in range(4):
        nr = r + mx[left[d]]
        nc = c + my[left[d]]
        d = rotate[d]
        
        if nr >= 0 and nr < N and nc >= 0 and nc < M and graph[nr][nc] == 0:
            backFlag = False
            break
            
    if backFlag == False:
        q.append( [nr,nc,d] )
    else:  # backFalg on
        br = r + mx[ back[d] ]
        bc = c + my[ back[d] ]
        if graph[br][bc] == 1: # 뒤에가 벽이라면 break.
            break
        else: # 뒤가 벽이 아니라면 뒤로가기
            q.append( [br,bc,d] )

result = 0
for i in range(N): result += graph[i].count(2)
print(result)