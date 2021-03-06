# 1198번: 삼각형으로 자르기
from itertools import combinations

def getArea( p1, p2, p3 ):
    first = ( p1[0] * p2[1] ) + ( p2[0] * p3[1] ) + ( p3[0] * p1[1] )
    second = ( p1[1] * p2[0] ) + ( p2[1] * p3[0] ) + ( p3[1] * p1[0] )
    re = (first-second) * 0.5
    return abs(re)
################################################################ 
N = int(input())
points = [ list(map(int, input().split())) for i in range(N) ]

result = 0 
for p1, p2, p3 in combinations( points, 3 ):
    area = getArea(p1, p2, p3)
    result = max(result,  area)
print( result )