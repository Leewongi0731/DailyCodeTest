# 이분탐색: 입국심사
def solution(n, times):
    times = sorted(times)
    
    # 최악의 경우 : 가장 느린 사람에게 모두 검사를 받는 경우
    left, right = 1, times[-1]*n
    answer = 0
    while left <= right:
        # 한명의 심사관에게 부여될 시간
        mid = (left + right) // 2
        
        check = 0
        for time in times:
            check += mid // time
            if check >= n: break
        
        # 해당 시간에 모든 n명의 심사를 받을 수 있다면
        # right를 줄여 부여시간을 감소시킴
        if check >= n:
            answer = mid
            right = mid - 1
        # 해당 시간에 모든 n명의 심사를 받을 수 없다면
        # left를 늘려 부여시간을 증가시킴
        else:
            left = mid + 1
            
    return answer