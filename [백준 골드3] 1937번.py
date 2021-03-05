# 1937번: 욕심쟁이 판다
n = int(input())
table = [ [] for i in range(n) ]
datas = []
for i in range(n):
    table[i] = list(map(int, input().split()))
    for j in range(n):
        datas.append( [ table[i][j], i, j ] )
        
datas = sorted( datas, reverse=True )
# 해당 위치에서 살수 있는 최대 일 수 
dp = [ [0]*n for i in range(n) ] 

# 판다가 이동 할 수 있는 형식
mx = [-1,1,0,0]
my = [0,0,-1,1]

# 최대 살 수 있는 일 수 
result = 0
for value, i, j in datas:
    roundValue = [0, 0, 0, 0, 1]
    for z in range(4):
        ii, jj = i + mx[z], j + my[z]
        if 0<=ii<n and 0<=jj<n and table[ii][jj] > value:
            # 자기위치 값보다, 인접값이 커야 이동가능
            roundValue[z] = dp[ii][jj] + 1
    dp[i][j] = max( roundValue )
    result = max( result, dp[i][j] )
print( result )