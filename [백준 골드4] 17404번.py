# 17404번: RGB거리 2
import sys
MAX_VALUE = 1234567890

N = int( input() )
cost = [ list( map(int, sys.stdin.readline().split()) ) for i in range(N) ]

result = MAX_VALUE
for firstColor in range(3):
    dp = [ [0] * 3 for i in range(N) ]
    for tmp in range(3):
        if tmp == firstColor: dp[0][tmp] = cost[0][tmp]
        else: dp[0][tmp] = MAX_VALUE

    for num in range(1, N, 1):
        for color in range(3):
            if num == N-1 and color == firstColor: 
                dp[num][color] = MAX_VALUE
                continue
            dp[num][color] = min( [ dp[num-1][beforColor] for beforColor in range(3) if color!=beforColor ] ) + cost[num][color]
    
    result = min( [result] + dp[N-1] )
print( result )