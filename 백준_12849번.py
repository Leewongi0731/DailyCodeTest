# 12849번: 본대 산책
MOD = 1000000007
D = int(input())

count = [1,0,0,0,0,0,0,0]

for _ in range(D):
    tmp = [ (count[1] + count[2]) % MOD, 
           (count[0] + count[2] + count[3]) % MOD, 
           (count[0] + count[1] + count[3] + count[4]) % MOD, 
           (count[1] + count[2] + count[4] + count[5]) % MOD , 
           (count[2] + count[3] + count[5] + count[7]) % MOD,
           (count[3] + count[4] + count[6]) % MOD, 
           (count[5] + count[7]) % MOD, 
           (count[4] + count[6]) % MOD ]

    count = tmp
print( count[0] )