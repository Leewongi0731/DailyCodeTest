# 정렬: H-Index
def solution(citations):
    citations = sorted( citations )
    if citations[-1] == 0: return 0
    
    answer = 0
    for index in range( len(citations) ):
        while len(citations)-index > answer and answer < citations[index]:
            answer+=1
        
        if len(citations)-index == answer:
            return answer
    return answer