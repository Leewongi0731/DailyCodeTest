# 10830번: 행렬 제곱
def squared( m1, m2 ):
    global N
    result = [ [0 for i in range(N)] for i in range(N) ]
    for i in range(N):
        for j in range(N):
            for z in range(N):
                result[i][j] += m1[i][z] * m2[z][j]
            result[i][j] %= 1000
    return result

def sol(b):
    if b == 1:
        return matrix
    
    r = sol( b // 2 )
    r = squared( r, r )
    
    if b % 2 == 1:
        r = squared( r, matrix )
        
    return r
########################################################################
N, B = list(map(int, input().split()))
matrix = [ list(map(int, input().split())) for i in range(N) ]

result = sol(B)

for i in range(N):
    for j in range(N):
        result[i][j] %= 1000

for r in result:
    print( ' '.join( map(str, r) ) )