# 14719번: 빗물
import heapq

H, W = list( map(int, input().split()) )
height = list( map(int, input().split()) )
n = len( height )
result, index = 0, 0

while index < n:
    if index < n-1 and height[ index ] > height[ index + 1 ]: # 줄어들기 시작하는 곳 -> 웅덩이가 생길 수 있는 곳
        leftHeap, rightHeap = [], [] # MAXHEAP, [value, index] 
        while index < n-1:
            if height[index] >= height[index+1]: # 감소하는 구간
                heapq.heappush( leftHeap, [ -height[index], index ] )
            else: # 증가하는 구간
                heapq.heappush( rightHeap, [ -height[index+1], index+1 ] )

                if -leftHeap[0][0] < -rightHeap[0][0]: # 첫 감소하는 구간보다, 높은 높이가 나오면 -> 웅덩이 채울 수 있음
                    targetHeigth = -leftHeap[0][0]
                    for i in range( leftHeap[0][1]+1, rightHeap[0][1], 1 ):  result += targetHeigth - height[i]
                    leftHeap, rightHeap = [], []
                    index += 1
                    break

            index += 1

        if len(rightHeap) != 0: # 웅덩이가 완성되지 않음 -> 울퉁불퉁하여 중간을 채워줘야 함
            left = heapq.heappop( leftHeap )
            right = heapq.heappop( rightHeap )
            targetHeigth = -right[0]
            for i in range(left[1]+1, right[1], 1): result += max( targetHeigth - height[i], 0 )

            while len(leftHeap)!=0 and len(rightHeap)!=0:
                while len(leftHeap)!=0 and left[1] != right[1]:
                    left = heapq.heappop( leftHeap )
                if left[1] != right[1]: break
                while len(rightHeap)!=0 and right[1] <= left[1]:
                    right = heapq.heappop( rightHeap )

                targetHeigth = min( -left[0], -right[0] )
                for i in range(left[1]+1, right[1], 1): result += max( targetHeigth - height[i], 0 )
    else:
        index += 1

print( result )