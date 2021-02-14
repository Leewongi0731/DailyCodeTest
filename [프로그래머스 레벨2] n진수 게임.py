# 2018 카카오 공채: n진수 게임
convert = {
    1 : '1', 2 : '2', 3 : '3', 4 : '4',
    5 : '5', 6 : '6', 7 : '7', 8 : '8',
    9 : '9', 10 : 'A', 11 : 'B', 12 : 'C',
    13 : 'D', 14 : 'E', 15 : 'F', 0 : '0'
}

def convertNum( num, n ):
    result = ""
    while num >= n:
        result = convert[num % n] + result
        num //= n
    result = convert[num] + result
    return result
    
def solution(n, t, m, p):
    targetLen = t * m
    nNum = "01"
    num = 2
    while len(nNum) < targetLen:
        # 찾아야하는 최대 문자열을 정하고 num을 늘려가며 진법변환을 실시
        nNum += convertNum( num, n )
        num += 1
    
    answer = ""
    for i in range(1, t+1):
        # 찾아야하는 index는 아래의 공식과 같다.
        searchIndex = (i-1)*m + p - 1
        answer += nNum[searchIndex]
        
    return answer