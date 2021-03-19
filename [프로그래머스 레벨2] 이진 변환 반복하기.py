# 월간 코드 챌린지: 이진 변환 반복하기
def solution(s):
    answer = [0, 0] # 변환의 횟수, 제거된 모든 0의 개수
    if s=="1": return answer
    if s=="0": return [1, 1]
    
    while s!="1":
        totalLen = len(s)
        zeroC = s.count("0")
        oneC = totalLen - zeroC
        
        answer[0] += 1
        answer[1] += zeroC
        
        
        s = bin( oneC )[2:]
    
    return answer