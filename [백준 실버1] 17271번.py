# 17271번: 리그 오브 레전설 (Small)
import operator as op
from functools import reduce

def nCr( n, r ):
    if n < 1 or r < 0 or n < r:
        raise ValueError
    r = min(r, n-r)
    numerator = reduce( op.mul, range(n, n-r, -1), 1 )
    denominator = reduce( op.mul, range(1, r+1), 1 )
    return numerator // denominator

N, M = list( map(int, input().split()) )
x = M-1
BCount = 0
result = 0

try:
    while True:
        result += nCr( N, BCount)
        N -= x
        BCount += 1
except:
    print( result % 1000000007 )