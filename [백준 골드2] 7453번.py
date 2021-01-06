# 7453번: 합이 0인 네 정수
N = int(input())
datas = [ [] for i in range(N) ]
for i in range(N):
    datas[ i ] = list(map(int,input().split()))
    
dp = {}
for i in range(N):
    for j in range(N):
        s = datas[i][2] + datas[j][3]
        if s not in dp.keys():
            dp[s] = 1
        else:
            dp[s] += 1
            
result = 0
for i in range(N):
    for j in range(N):
        s = datas[i][0] + datas[j][1]
        try:
            result += dp[-s]
        except:
            pass
print(result)