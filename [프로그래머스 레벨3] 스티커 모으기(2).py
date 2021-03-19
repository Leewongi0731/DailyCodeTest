# Summer/Winter Coding: 스티커 모으기(2)

def solution(sticker):
    N = len( sticker )
    if N==1: return sticker[0]
    if N==2: return max(sticker)
    
    # use first sticker
    dp1 = [ [0,0] for i in range(N) ]
    dp1[0][True] = dp1[1][False] = sticker[0]
    index = 2
    while index < N-1:
        dp1[index][True] = dp1[index-1][False] + sticker[index]
        dp1[index][False] = max( dp1[index-1][False], dp1[index-1][True] )
        index += 1
    answer1 = max( dp1[N-2] )
    
    # don't use first sticker
    dp2 = [ [0,0] for i in range(N) ]
    index = 1
    while index < N:
        dp2[index][True] = dp2[index-1][False] + sticker[index]
        dp2[index][False] = max( dp2[index-1][False], dp2[index-1][True] )
        index += 1
    answer2 = max( dp2[N-1] )
    
    return max( answer1, answer2 )