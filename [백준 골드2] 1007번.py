# 1007번: 벡터 매칭
from itertools import combinations

T = int(input())
for _ in range(T):
    N = int(input())
    points = [ list(map(int, input().split())) for i in range(N) ]
    
    if N == 2:
        x = points[0][0] - points[1][0]
        y = points[0][1] - points[1][1]
        result =  pow( x*x + y*y, 1/2 )
        print( "{:.7f}".format(result) )
        continue

    allSumX, allSumY = 0, 0
    for x, y in points:
        allSumX += x
        allSumY += y
    
    result = 9223372036854775807
    for startPoints in combinations( points, N//2 ):
        startSumX, startSumY = 0, 0
        for x, y in startPoints:
            startSumX += x
            startSumY += y
        
        endSumX = allSumX - startSumX
        endSumY = allSumY - startSumY
        
        x = endSumX - startSumX
        y = endSumY - startSumY
        result = min( result, pow( x*x + y*y, 1/2 ) )
    print( "{:.7f}".format(result) )