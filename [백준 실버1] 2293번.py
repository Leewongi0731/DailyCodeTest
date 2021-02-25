# 2293번: 동전 1
n, k = list(map(int, input().split()))
datas = [ int(input()) for i in range(n) ]
datas = list(set(sorted(datas)))

dp=[0 for i in range(k+1)]
dp[0] = 1

for data in datas:
    for index in range( 0, k-data+1 ):
        dp[ data+index ] += dp[ index ]
        
print( dp[-1] )