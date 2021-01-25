# 18428번: 감시 피하기
from itertools import combinations
from collections import deque

def findStudent( i, j, N ):
    for x in range(4):
        ii, jj = i, j
        while True:
            ii, jj = ii+mx[x], jj+my[x]
            if ii >= 0 and ii < N and jj >= 0 and jj < N:
                if graph[ii][jj] == 'S':
                    return False
                elif graph[ii][jj] == 'O':
                    break
            else:
                break
    return True
#################################################################

N = int(input())
graph = [ [] for i in range(N) ]
teacher = []
wall = []
for i in range(N):
    graph[i] = input().split()
    for j in range(N):
        if graph[i][j] == 'T': teacher.append( [i, j] )
        elif graph[i][j] == 'X': wall.append( [i, j] )

mx = [-1,1,0,0]
my = [0,0,-1,1]
for com in combinations(wall, 3):
    for c in com: graph[c[0]][c[1]] = 'O'
    
    result = "YES"
    for ti, tj in teacher:
        if findStudent(ti, tj, N) == False:
            result = "NO"
            break
    if result == "YES": break
        
    for c in com: graph[c[0]][c[1]] = 'X'
print( result )