# 2186번: 문자판
import sys

def sol(i, j, index):
    global N, M, K
    if index+1 == len(word):  visited[i][j][index] = 1
    if visited[i][j][index] != -1: return visited[i][j][index]
    
    cnt = 0
    for k in range(1, K+1):
        for z in range(4):
            ni = i + mx[z]*k
            nj = j + my[z]*k
            
            if 0<=ni<N and 0<=nj<M and table[ni][nj] == word[index+1]:
                cnt += sol(ni, nj, index+1)
    visited[i][j][index] = cnt
    return visited[i][j][index]
######################################################################
N, M, K = list(map(int, input().split()))
table = [ list(sys.stdin.readline().rstrip()) for i in range(N) ]
word = list( input() )
visited = [ [ [-1]*len(word) for i in range(M) ] for i in range(N) ]
mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]

result  = 0
for i in range(N):
    for j in range(M):
        if table[i][j] == word[0]:
            result +=  sol(i, j, 0)
print(result) 