# 연습문제: 최댓값과 최솟값
def solution(s):
    s = list(map(int, s.split(' ') ) )
    minVal = min(s)
    maxVal = max(s)
    
    return str(minVal) + ' ' + str(maxVal)