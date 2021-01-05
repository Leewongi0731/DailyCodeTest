# 2467번: 용액
def binary_search(target, N):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return True, mid # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return False, start
#########################################
N = int(input())
data = list(map(int, input().split()))

result = []
if data[-1] <= 0: # 모두 아칼리
    result = [ data[-2], data[-1] ]
elif data[0] >= 0: # 모두 산성
    result = [ data[0], data[1] ]
else:
    right = binary_search(0, N)[1]
    left = right - 1
    result = [ data[left], data[right] ]
    minValue = abs( data[left] + data[right] )
    
    if left > 0 and abs( data[left-1] + data[left] ) < minValue: # 아칼리 / 아칼리가 최소일때
        minValue = abs( data[left-1] + data[left] )
        result = [ data[left-1], data[left] ]
        
    if right < N - 1 and abs( data[right] + data[right+1] ) < minValue: # 산성 / 산성이 최소일때
        minValue = abs( data[right] + data[right+1] )
        result = [ data[right], data[right+1] ]
        
    if data[right] == 0 and data[right+1] < minValue:
        result = [ data[right], data[right+1] ]
        minValue = data[right+1]
        right += 1
    
    while left>=0 and right<N and minValue > 0:
        value = data[left] + data[right]
        absValue = abs(value)
        if absValue < minValue:
            minValue = absValue
            result = [ data[left], data[right] ]
            
        # move
        if value > 0: # left move
            left -= 1
        else: # right move
            right += 1
        
print( ' '.join( map(str, result) ) )