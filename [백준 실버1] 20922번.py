# 20922번: 겹치는 건 싫어
# 2021 ICPC Sinchon Winter Algorithm Camp Contest - 초급 : C

N, K = list(map(int, input().split()))
datas = list(map(int, input().split()))

lenV = [ 0 for i in range( N ) ]
indexs = [ [] for i in range(100001) ]
popStartIndex = 0
count = 0
for i, data in enumerate(datas):
    if len( indexs[data] ) +1 > K :
        popLastIndex = indexs[data][0]
        for popIndex in range( popStartIndex, popLastIndex+1 ):
            popVal = datas[popIndex]
            indexs[popVal].pop(0)
            count -= 1
        popStartIndex = popLastIndex+1
            
    indexs[data].append( i )
    count += 1
    lenV[ i ] = count
    
print( max(lenV) )