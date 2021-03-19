# Summer/Winter Coding: 영어 끝말잇기
def solution(n, words):
    answer = [0, 0]
    
    useWord = set()
    loopNum = 1
    turn = 0
    beforEndChr = words[0][0]
    for word in words:
        if word in useWord or beforEndChr != word[0]:
            answer = [ turn+1, loopNum ]
            break
        
        useWord.add( word )
        beforEndChr = word[-1]
        
        turn += 1
        turn %= n
        if turn == 0: loopNum += 1
    
    return answer