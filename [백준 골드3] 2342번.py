# 2342번: Dance Dance Revolution
import sys

cost = [
    [0,2,2,2,2],
    [2,1,3,4,3],
    [2,3,1,3,4],
    [2,4,3,1,3],
    [2,3,4,3,1]
]

datas = list(map(int, input().split()))
result = 0
reData = [ datas[0] ]
for i in range(1, len(datas)-1):
    if reData[-1] == datas[i]:  result += 1
    else: reData.append( datas[i] )
datas = [0] + reData

# 시작앞에 0을 추가. (더미 데이터)
# 시작. 왼/오 0에서 cost는 위에서 처리한, 연속적인 값 갯수
size = len(datas)
dp = [ [ [ sys.maxsize ]*5 for i in range(5) ] for i in range( size ) ]
dp[0][0][0] = result

for i in range(1, size):
    for l in range(5):
        for r in range(5):
            # 오른발 왼발 같이 놓을때x
            if l==r:  continue
            if datas[i]!=l and datas[i]!=r: continue
            
            for z in range(5):
                if (l==datas[i]): # 왼발이 z에서 l로 움직임
                    dp[i][l][r] = min(dp[i][l][r], dp[i-1][z][r]+ cost[z][l] )
                else:  # 오른발이 z에서 l로 움직임
                    dp[i][l][r] = min(dp[i][l][r], dp[i-1][l][z]+ cost[z][r] )

# 마지막 위치에서 최소 cost
print(  min( [min( dp[-1][i] ) for i in range(5)] )  )