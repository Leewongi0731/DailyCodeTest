# 2449번: 전구
import sys

N, K = list(map(int, input().split()))
datas = list(map(int, input().split()))

reData = [ datas[0] ]
for i, data in enumerate( datas[1:] ):
    i += 1
    if data != reData[-1]:
        reData.append( data )
        
datas = reData
N = len(datas)

dp = [ [0]*N for i in range(N) ]

# start / end 
# 0,0
# 0 1 -> 0 0 + 1 1
# 1 2 -> 1 1 + 2 2
# 0 2 -> 0 0 + 1 2
#     -> 0 1 + 2 2
# 2 3 -> 2 2 + 3 3
# 1 3 -> 1 1 + 2 3
#     -> 1 2 + 3 3
#  ........
# 이런식으로 DP값을 찾아야 함으로 아래와 같이 start/end를 탐색
for end in range(N):
    for start in range( end-1, -1, -1 ):
        dp[start][end] = sys.maxsize
        for mid in range( start, end ):
            # 최종적으로 왼쪽은 datas[start]으로 통일, 
            # 오른쪽은 datas[mid+1] 지점으로 통일.
            # datas[start] = datas[mid+1]이라면, 붙히는데 cost 발생 X
            # datas[start] != datas[mid+1]이라면 오른쪽을 왼쪽으로 맞추는데 1번 뒤집어야 함
            if datas[start] == datas[mid+1]: 
                dp[start][end] = min( dp[start][end], dp[start][mid] + dp[mid+1][end] )
            else:
                dp[start][end] = min( dp[start][end], dp[start][mid] + dp[mid+1][end] + 1 )
print( dp[0][N-1] )