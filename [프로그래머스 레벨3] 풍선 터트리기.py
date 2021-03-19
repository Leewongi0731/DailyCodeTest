# 월간 코드 챌린지: 풍선 터트리기
# 번호가 더 작은 풍선을 터트리는 행위는 최대 1번
# 최후까지 남기는 것이 가능한 풍선들의 개수를 return 하도록 solution 함수
def solution(a):
    minV = min(a)
    index = a.index( minV )
    answer = 1 # 더 작은 풍선을 한번도 안터트리면, 최소값이 최종적으로 남음

    # 가장 최소값을 기준으로 왼쪽만 보기 ( 오른쪽의 최소값과의 비교에서 전부 제거 가능 )
    left = []
    for i, data in enumerate( a[:index] ):
        left.append( [data, i] )
    left = sorted( left )
    
    leftMinValIndex = index
    for data, i in left:
        if i < leftMinValIndex:
            # 해당 값보다 작은 값이 왼쪽에 없다.
            # 여기까지 전체 a list에서 가장 작은 값을 가져와서, 해당값과 비교에서 가장 작은 값을 없애면,
            # 해당값이 최종적으로 남음
            leftMinValIndex = i
            answer += 1
    
    # 가장 최소값을 기준으로 오른쪽만 보기 ( 왼쪽의 최소값과의 비교에서 전부 제거 가능 )
    right = []
    for i, data in enumerate( a[index+1:] ):
        right.append( [data, index+i+1] )
    right = sorted( right )
    
    rightMinValIndex = index
    for data, i in right:
        if i > rightMinValIndex:
            # 해당 값보다 작은 값이 오른쪽에 없다.
            # 여기까지 전체 a list에서 가장 작은 값을 가져와서, 해당값과 비교에서 가장 작은 값을 없애면,
            # 해당값이 최종적으로 남음
            rightMinValIndex = i
            answer += 1
                
    return answer