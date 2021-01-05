# 13460번: 구슬 탈출 2
from collections import deque

def move(i, j, dx, dy):
    c = 0
    while board[i + dx][j + dy] != "#" and board[i][j] != "O":
        i += dx
        j += dy
        c += 1
    return i, j, c

def bfs():
    while q:
        ri, rj, bi, bj, d = q.popleft()
        if d > 10:
            break
        for i in range(4): # [1,0] : 오른쪽, [-1,0] : 왼쪽, [0,-1] : 위쪽, [0,1] : 아래쪽
            nri, nrj, rc = move(ri, rj, dx[i], dy[i])
            nbi, nbj, bc = move(bi, bj, dx[i], dy[i])
            if board[nbi][nbj] != "O":
                if board[nri][nrj] == "O":
                    print(d)
                    return
                if nri == nbi and nrj == nbj:
                    if rc > bc: # RED 이동거리가 길다 -> RED가 BLUE이전에 멈춰야 한다.
                        nri -= dx[i]
                        nrj -= dy[i]
                    else:
                        nbi -= dx[i]
                        nbj -= dy[i]
                if not visit[nri][nrj][nbi][nbj]:
                    visit[nri][nrj][nbi][nbj] = True
                    q.append([nri, nrj, nbi, nbj, d + 1])
    print(-1)
################################################################################################
N, M = list(map(int, input().split()))
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
visit = [[[[False] * M for i in range(N)] for i in range(M)] for i in range(N)]
board = []

for i in range(N):
    a = list(input())
    board.append(a)
    for j in range(M):
        if a[j] == "R":
            ri, rj = i, j
        if a[j] == "B":
            bi, bj = i, j
q = deque()
q.append([ri, rj, bi, bj, 1])
visit[ri][rj][bi][bj] = True
bfs()