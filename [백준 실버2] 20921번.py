# 20921번: 그렇고 그런 사이
# 2021 ICPC Sinchon Winter Algorithm Camp Contest - 초급 : B

N, K = list(map(int, input().split()))
datas = [ i for i in range(1, N+1)]

result = []
for i in range( N ):
    maxV = N - i -1
    target = min( K, maxV )
    K -= target
    
    result.append( datas.pop(target) )
    
print( ' '.join( map(str, result) ) )