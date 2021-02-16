# 연습문제: 야근 지수
def solution(n, works):
    # 각 인자의 제곱의 합이 가장 작을려면, 각 인자가 모두 비슷 값이여야 함
    workSum = sum(works)
    if workSum <= n: return 0
    if len(works) == 1: return (works[0]-n)**2
    
    works = sorted( works )
    targetIndex = len(works) - 1
    maxValueCount = 1    # 감소시켜줘야하는 인자 갯수
    plusOneCount = 0     # 최대 값 works[targetIndex] 보다 하나 큰 값의 갯수
    while n > 0:
        if targetIndex != 0 and works[targetIndex] == works[targetIndex-1]:
            # 만약 앞의 인자랑 값이 같다면, 앞의 인자가 줄어들때 같이 줄어들도록 설정
            targetIndex -= 1
            maxValueCount += 1
        else:
            if n - maxValueCount >= 0:
                n -= maxValueCount
            else:
                plusOneCount = maxValueCount - n
                n = 0
            works[targetIndex] -= 1
    
    answer = ( works[targetIndex] ** 2 ) * (maxValueCount-plusOneCount) + ( (works[targetIndex]+1) ** 2 ) * plusOneCount
    for i in range( 0, targetIndex ):
        answer += works[i] ** 2
    return answer