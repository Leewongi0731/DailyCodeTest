# 2473번: 세 용액
# 2467번문제와 비슷, List를 크기별로 정렬하고, 앞에서부터 하나씩 list[i]를 답안으로 넣고, list[i+1:]에서 2개 합 -list[i]를 찾는다.
def binary_search(target, data, start, end):
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
data = sorted( data )

result = []
if data[-1] <= 0: # 모두 아칼리
    result = [ data[-3], data[-2], data[-1] ]
elif data[0] >= 0: # 모두 산성
    result = [ data[0], data[1], data[2] ]
else:
    result = [ data[0], data[1], data[2] ]
    minValue = abs( data[0] + data[1] + data[2] )
    for i in range( N-2 ):
        if data[i] > 0:
            if abs( data[i] + data[i+1] + data[i+2] ) < minValue:
                minValue = abs( data[i] + data[i+1] + data[i+2] )
                result = [ data[i], data[i+1], data[i+2] ]
            break
            
        target = -data[i]
        right = binary_search(target/2, data, i+1, N-1)[1]
        left = right - 1
        
        if left > i+1 and abs( data[i] + data[left-1] + data[left] ) < minValue:
            minValue = abs( data[i] + data[left-1] + data[left] )
            result = [ data[i], data[left-1], data[left] ]

        if right < N-1 and abs( data[i] + data[right] + data[right+1] ) < minValue:
            minValue = abs( data[i] + data[right] + data[right+1] )
            result = [ data[i], data[right], data[right+1] ]
        
        while left > i and right < N and minValue > 0:
            value = data[left] + data[right]
            absValue = abs( data[i] + value)
            if absValue < minValue:
                minValue = absValue
                result = [ data[i], data[left], data[right] ]

            # move
            if value > target: # left move
                left -= 1
            else: # right move
                right += 1
        
print( ' '.join( map(str, result) ) )