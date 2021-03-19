# 월간 코드 챌린지: 삼각 달팽이
def solution(n):
    table = [ [0 for i in range(n)] for i in range(n) ]
    for i in range(n): table[i][0] = i+1
    
    turn = 1
    i, j = n-1, 0
    modes = [ [1, 0], [0,1], [-1,-1] ] # 대각선 내려가기, 오른쪽 이동, 대각선 올라가기
    val = n
    while turn < n:        
        mx, my = modes[ turn % 3 ]
        
        for z in range( n-turn ):
            val += 1
            i, j = i+mx, j+my
            table[i][j] = val
            
        turn += 1
    
    answer = []
    for i in range(n):
        answer += table[i][:i+1]
    
    return answer