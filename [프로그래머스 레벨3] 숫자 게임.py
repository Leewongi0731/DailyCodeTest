# Summer/Winter Coding: 숫자 게임
from bisect import bisect_left

def solution(A, B):
    B = sorted( B )
    
    answer = 0
    for a in A:
        index = bisect_left( B, a+1 )
        if index < len(B):
            answer += 1
            B.pop( index )
    
    return answer