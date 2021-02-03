# 1202번: 보석 도둑
import sys
from bisect import bisect_left # 값보다 같거나 큰 값 찾는 binary serach

def getIndex( i ):
    if bagIndex[i] == i: return i
    else: return getIndex( bagIndex[i] )
######################################################################################################
N, K = list(map(int, input().split()))
datas = [ list(map(int, sys.stdin.readline().split())) for i in range(N) ] # weight, value
bag = [ int(sys.stdin.readline()) for i in range(K) ]

datas = sorted( datas, key=lambda x : x[1], reverse=True ) # vlaue 내림차순
bag.sort() # 오른차순
bagIndex = [ i for i in range(K+1) ]

result = 0
for weight, value in datas:
    index = bisect_left( bag, weight )
    
    try:
        realIndex = getIndex( index )
        if realIndex == K: continue
        result += value
        bagIndex[realIndex] = bagIndex[index] = bagIndex[realIndex+1]
    except: # 불가능
        pass
print( result )