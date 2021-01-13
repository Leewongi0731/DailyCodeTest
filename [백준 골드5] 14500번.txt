# 14500번: 테트로미노
N, M = list(map(int, input().split()))
graph = [ list(map(int, input().split())) for i in range(N) ]

# 모든 도형정보
moves = [ 
    [ [1,0], [2,0], [3,0] ], [ [0,1],[0,2],[0,3] ], 
    [ [0,1],[1,0],[1,1] ],
    [ [1,0],[2,0],[2,1] ], [ [1,0],[0,1],[0,2] ], [ [0,1],[1,1],[2,1] ], [ [0,1],[0,2],[-1,2] ],
    [ [1,0],[1,1],[1,2] ], [ [0,1],[-1,1],[-2,1] ], [ [0,1],[0,2],[1,2] ], [ [0,1],[1,0],[2,0] ],
    [ [1,0],[1,-1],[2,-1] ], [ [0,1],[1,1],[1,2] ],
    [ [1,0],[1,1],[2,1] ], [ [0,1],[-1,1],[-1,2] ],
    [ [0,1],[0,2],[1,1] ], [ [1,0],[2,0],[1,1] ], [ [0,1],[0,2],[-1,1] ], [ [0,1],[-1,1],[1,1] ], 
]

result = 0
for i in range(N):
    for j in range(M):
        for move in moves:
            isPossible = True
            tmp = graph[i][j]
            
            for m in move:
                if i+m[0] < 0 or i+m[0] >= N or j+m[1] < 0 or j+m[1] >= M:
                    isPossible = False
                    break
                tmp += graph[ i+m[0] ][ j+m[1] ]
                
            if isPossible == True and tmp > result:
                result = tmp
print( result )