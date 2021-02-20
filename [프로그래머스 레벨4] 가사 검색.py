# 2020 카카오 공채: 가사 검색
from bisect import bisect_left

def getCount( data, search ):
    # bisect_left 모듈을 사용하여 정렬된 data list에서 해당 문자열이 시작 할 수 있는 지점을 찾음
    left = bisect_left( data, search )
    right = len(data)-1
    count = 0
    
    while left <= right:
        mid = (left+right)//2
        target = data[mid]
        
        passBit = True
        for i in range( len(search)-1, -1, -1 ):
            if target[i] != search[i]: 
                passBit = False
                break
        
        if passBit == True:
            # mid 값이 성공이라는 것은 left ~ mid 까지가 모두 통과라는 것
            count += mid - left + 1
            left = mid + 1
        else:
            # mid 값이 실패라는 것은 mid~right 까지가 모두 실패라는 것
            right = mid - 1
    return count 
    
def solution(words, queries):
    word = [[] for i in range(10001)]
    reveredWord = [[] for i in range(10001)]
    for w in words: 
        # 각 word를 word길이에 따라 분류함
        # ???로 시작하는 querie와 뒤에 ???가 붙는 querie를 따로 처리하기 위해 word, reveredWord 두개로 나누어 저장
        len_w = len(w)
        word[len_w].append(w)
        reveredWord[len_w].append(w[::-1])
        
    for i in range(1, 10001):
        # 각 word집함을 모두 정렬해둠
        word[i] = sorted( word[i] )
        reveredWord[i] = sorted( reveredWord[i] )
        
    answer = [0 for i in range(len(queries))]
    for i, q in enumerate(queries):
        q_len = len(q)
        questStart = q.find('?')
        questEnd = q_len - q[::-1].find('?') - 1
        
        # 만약 모든 질의에 모든 것이 ?라면, 해당 길이만큼의 문자열은 모두 통과
        if q_len == questEnd-questStart+1: count = len( word[q_len] )
        elif questStart != 0:
            # 끝이 ?로 끝나는 질의
            search = q[:questStart]
            data = word[q_len]
            count = getCount( data, search )
        else:
            # 시작이 ?로 시작하는 질의
            q = q[::-1]
            questStart = q.find('?')
            
            search = q[:questStart]
            data = reveredWord[q_len]
            count = getCount( data, search )
            
        answer[i] = count
    
    return answer