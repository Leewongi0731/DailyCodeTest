# 탐욕법(Greedy): 구명보트
def solution(people, limit):
    if len(people)==1: return 1
    
    people =  sorted( people )
    
    leftIndex = 0
    rightIndex = len(people)-1
    answer = 0
    while leftIndex < rightIndex:
        s = people[leftIndex] + people[rightIndex]
        
        # 가장 큰 값은 조합없이, 혼자 가야하는 경우
        if s > limit: 
            answer += 1
            rightIndex -= 1
            continue
        
        # 가장 큰사람과, 작은 사람이 최대 몇 명까지 탈 수 있는지 확인
        for i in range(  leftIndex+1, rightIndex): 
            if s + people[i] <= s:
                leftIndex = i
                s += people[i]
            else:
                break
                
        leftIndex += 1
        rightIndex -= 1
        answer += 1
        
    if leftIndex == rightIndex: answer += 1
    
    return answer