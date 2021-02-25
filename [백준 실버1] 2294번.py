# 2294번: 동전 2
n, k = list(map(int, input().split()))
datas = [ int(input()) for i in range(n) ]
datas = list(set(datas))

dp = [ 123456789 for i in range(k+1) ] # 금액 -> 동전 갯수
dp[0] = 0

for data in datas:
    for index in range( 0, k-data+1 ):
        dp[ data+index ] = min( dp[ data+index ], dp[ index ] + 1 ) 

if dp[-1] == 123456789: print(-1)
else: print( dp[-1] )