# 14499번: 주사위 굴리기
N, M, x, y, K = list(map(int, input().split()))
graph = [ list(map(int, input().split())) for i in range(N) ]
moveList = list(map(int, input().split()))
now = [ 1, 4, 2, 6, 3, 5 ] # botton, 동쪽, 서쪽, 북쪽, 남쪽, top
swiching = {1:2, 2:1, 3:4, 4:3} # 이동하면 바뀌는 값 : 위/아래/가는방향/반대방향
number = [ 0, 0, 0, 0, 0, 0, 0 ] # 각 주사위에 기입된 기본 값 index 0은 사용안함

for move in moveList:
    mx, my = x, y
    if move == 1: my += 1   # 동
    elif move == 2: my -= 1 # 서
    elif move == 3: mx -= 1 # 북
    else: mx += 1        # 남
    
    if mx < 0 or mx >= N or my < 0 or my >= M: # 이동한 범위가 graph 넘어간다면 적용 X
        continue
    else:
        x, y = mx, my
    
    
    # new Bottom / newTop / old Botton / oldTop
    now[0], now[-1], now[ swiching[move] ], now[ move ] = now[ move ], now[ swiching[move] ], now[0], now[-1]
    
    if graph[x][y] == 0:
        graph[x][y] = number[ now[0] ]
    else:
        number[ now[0] ] = graph[x][y]
        graph[x][y] = 0
    
    print( number[ now[-1] ] )