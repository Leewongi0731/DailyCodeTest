# 2020 카카오 공채: 문자열 압축
def solution(s):
    answer = len(s) # 최대치로 설정

    for splitNum in range( 1, len(s)//2+1 ):
        check = [ 1 for _ in range( len(s)//splitNum) ]
        check[-1] = 0
        splitDatas = [ s[i::splitNum] for i in range(splitNum) ]
        
        for splitData in splitDatas:
            for i in range( len(check)-1 ):
                if check[i] == 1 and splitData[i] != splitData[i+1]:
                    check[i] = 0
        
        tmp = len(s) % splitNum # 묶일 수 없는 뒷 자리 남은 갯수
        sequenceCount = 1 # 반복하는 갯수
        for i in range(len(check)):
            if check[i] == 1:  sequenceCount += 1
            else:
                if sequenceCount != 1: tmp += len( str(sequenceCount) )
                sequenceCount = 1
                tmp += splitNum
                
        answer = min( answer, tmp )
        
    return answer