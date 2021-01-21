# 2019 카카오 공채: 무지의 먹방 라이브
from collections import Counter
import heapq

def solution(food_times, k):
    result = 1
    counter =  Counter( food_times )
    heap = []
    for key in counter.keys():
        heapq.heappush( heap, [ key, counter[key] ] )
    
    length = len( food_times )
    beforMinValue = 0
    while True:
        # 더이상 먹을 것이 없음
        if len( heap ) == 0: 
            result = -1
            break

        # k가 남은 음식 중 가장 빨리먹을 수 있는 음식을 다 먹을만큼 크다면, k값을 해당음식을 다 먹고 첫번째 음식으로 돌아옴
        minValue, valueCount = heapq.heappop( heap )
        if k - length * (minValue - beforMinValue) >= 0:
            k -= length * (minValue - beforMinValue)
            beforMinValue = minValue
            length -= valueCount
            
        # k가 남은 음식 중 가장 빨리먹을 수 있는 음식을 다 먹지 못하는 값이라면, 남음 음식 길이로 나누고 몇 번째 음식에서 정전이 일어나는지 찾음
        else:
            k %= length
            for i, time in enumerate( food_times ):
                if time >= minValue:
                    if k == 0: break # 정전이 일어나기 직전 먹던 음식이 아닌, 정전 후에 먹을 음식을 찾는 것이므로 0체크를 먼저함
                    k -= 1
            result = i + 1 # 결과는 index가 아닌 "몇 번째"를 묻는 것이므로 +1를 함
            break
    
    return result