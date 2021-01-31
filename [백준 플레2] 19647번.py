# 19647번: Unique Solution
import sys

N = int(input())
problem = [ [] for i in range(N)]
solution = [ [] for i in range(N+1) ]

for i in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    
    for s in data[1:]:
        problem[i].append( s )
        solution[s].append(i)
        
count = 0
state = True
result = [0 for i in range(N)]
while count < N and state:
    state = False
    
    for problemIndex in range(N):
        if len( problem[problemIndex] ) == 1:
            count += 1
            state = True
            
            solutionIndex = problem[problemIndex][0]
            result[ problemIndex ] = solutionIndex
            
            for removeIndex in solution[ solutionIndex ]:
                problem[ removeIndex ].remove( solutionIndex )
            
            continue

if count == N:
    print( 1 )
    print( ' '.join(map(str, result)) )
else:
    print(-1)