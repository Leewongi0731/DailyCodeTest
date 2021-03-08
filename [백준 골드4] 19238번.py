# 19238번: 스타트 택시
import heapq
# 어떤 승객을 태운것인가 조건
# 1. 백준이 태울 승객을 고를 때는 현재 위치에서 최단거리가 가장 짧은 승객을 고른다.
# 2. 그런 승객이 여러 명이면 그중 행 번호가 가장 작은 승객
# 3. 그런 승객도 여러 명이면 그중 열 번호가 가장 작은 승객을

# 어떤 조건을 통과해야 하는가
# 1. 한 승객을 목적지로 성공적으로 이동시키면, 그 승객을 태워 이동하면서 소모한 연료 양의 두 배가 충전
# 2. 승객을 목적지로 이동시킨 동시에 연료가 바닥나는 경우는 실패한 것으로 간주하지 않는다

N, M, fuel = list(map(int, input().split()))
table = [ list(map(int, input().split())) for i in range(N) ] # 0은 빈칸, 1은 벽
pos = list(map(int, input().split())) # 현재위치
pos[0] -= 1
pos[1] -= 1
guests = [ [] for i in range(M) ] # 손님
for i in range(M):
    guest = list(map(int, input().split()))
    guest[0] -= 1
    guest[1] -= 1
    guest[2] -= 1
    guest[3] -= 1
    guest.append( guest[0]*N+guest[1] ) # 출발 node / 도착 node번호 추가
    guest.append( guest[2]*N+guest[3] ) # 출발 node / 도착 node번호 추가
    guests[i] = guest
guests = sorted( guests ) # 동일 길이, 행번호, 열번호 낮은순으로 검색하기 위해
checked = [ False for i in range(M) ] # 손님 확인용

# INIT graph
NODENUM = N*N
graph = [ [123456789 for i in range(NODENUM)] for i in range(NODENUM) ]
for i in range(NODENUM): graph[i][i] = 0
mx, my = [-1,1,0,0], [0,0,-1,1]
for i in range(N):
    for j in range(N):
        if table[i][j] == 0:
            node = i*N+j
            for z in range(4):
                ii, jj = i+mx[z], j+my[z]
                if 0<=ii<N and 0<=jj<N and table[ii][jj]==0:
                    nextNode=ii*N+jj
                    graph[node][nextNode] = 1
                    
# 최단거리 계산
for k in range(NODENUM):
    for i in range(NODENUM):
        for j in range(i+1, NODENUM):
            graph[i][j] = graph[j][i] = min( graph[i][j], graph[i][k]+graph[k][j] )
    


count = 0
while count < M:
    heap = []
    nowNode = pos[0]*N+pos[1]
    
    for i in range(M):
        if checked[i]==False:
            d1Cost = graph[ nowNode ][ guests[i][4] ]
            heapq.heappush( heap, [d1Cost, i] )
            if d1Cost==0: break    
            
    # d1Cost : 택시 위치에서 -> 승객위치
    # d2Cost : 승객위치 -> 승객 목적지
    d1Cost, nextGuestIndex = heap[0]
    d2Cost = graph[ guests[nextGuestIndex][4] ][ guests[nextGuestIndex][5] ]  
    
    print( count, d1Cost, d2Cost, d1Cost+d2Cost, fuel )
    
    if d1Cost + d2Cost > fuel:# 불가능
        break 
    else: # 가능
        checked[ nextGuestIndex ] = True
        # 승객을 태워 이동하면서 소모한 연료 양의 두 배가 충전
        fuel -= d1Cost + d2Cost
        fuel += d2Cost*2
        pos = [ guests[nextGuestIndex][2], guests[nextGuestIndex][3] ]
    count += 1
    
if count==M: print( fuel )
else: print(-1)