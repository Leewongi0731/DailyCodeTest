# 1080번: 행렬
def checkEquality():
    for i in range(N):
        for j in range(M):
            if A[i][j] !=B[i][j]:
                return 0
    return 1
############################################################################
N, M = list( map(int, input().split()) )
A = [ list(map( int, list(input()) )) for i in range(N) ]
B = [ list(map( int, list(input()) )) for i in range(N) ]
switching = [1, 0]

count = 0
for i in range( 0, N - 2, 1 ):
    for j in range( 0, M - 2, 1 ):
        if A[i][j] != B[i][j]:
            for ii in range(i, i+3):
                for jj in range(j, j+3):
                    A[ii][jj] = switching[ A[ii][jj] ]
            count += 1
            
if checkEquality(): print(count)
else: print(-1)