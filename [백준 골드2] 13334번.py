# 13334번: 철로
import heapq

n = int(input())
datas = [ sorted( list(map(int, input().split())) ) for i in range(n) ]
d = int(input())

datas = [ data for data in datas if data[1]-data[0] <= d ]
datas = sorted(datas)
n = len(datas)
if n<=1: print(n)
else:
    dp = [ 0 for i in range(n) ]
    dp[0] = 1
    impossibleHeap = [] # [끝나는 위치, index] 데이터 minHeap으로 저장
    endIndex = 1
    for index in range( len(datas) ):
        start, end = datas[index][0], datas[index][0] + d
        if index != 0:
            # 이전 시작점보다 시작점이 한칸 전진하였으므로 -1
            dp[index] = dp[index-1]-1
            # 이전의 시작점과 같다면 체크하지 않아 됨
            if datas[index] == datas[index-1]: continue
        
        # impossibleHeap check
        while impossibleHeap:
            if impossibleHeap[0][0] > end: break
            if impossibleHeap[0][1] >= index: dp[index]+=1
            heapq.heappop( impossibleHeap )
            
        
        # endIndex에서 몇 칸 더 갈 수 있는지 확인
        for i in range( endIndex, n ):
            # 해당 값의 끝 점이 범위 start~end 사이에 있다면 dp값 +1
            if datas[i][1] <= end: dp[index] += 1
            # 해당 값이 범위안에는 없지만, 공통 범위가 있다면 impossibleHeap에 push
            elif datas[i][0] <= end: heapq.heappush( impossibleHeap, [datas[i][1], i] )
            # 범위의 아예 밖에 있다면 break
            else:
                endIndex = i
                break
            
            if i == n-1: endIndex = n
            
    print( max(dp) )