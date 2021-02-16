# 그래프: 순위
import copy

def solution(n, results):
    winLoseCount = [ [ set(), set() ] for i in range(n+1) ]
    tmpCount = None
    
    while tmpCount != winLoseCount:
        tmpCount = copy.deepcopy( winLoseCount )

        for win, lose in results:
            winLoseCount[win][0].add( lose )
            for w in winLoseCount[win][1]: # 패배한 사람은, 이긴사람을 저번에 이긴사람에게도 패배한 것임
                winLoseCount[w][0].add( lose )
                winLoseCount[lose][1].add( w )
                
            winLoseCount[lose][1].add( win )
            for l in winLoseCount[lose][0]: # 이긴 사람은, 패배한 사람에게 저번에 패배한 사람에게도 이긴 것임
                winLoseCount[l][1].add( win )
                winLoseCount[win][0].add( l )
                
    answer = 0
    for i in range(1, n+1):
        # 자신의 순위가 확정되었다는 것은, 해당 사람 입장에서 이긴 사람의 수와, 진 사람의수의 합이 n-1이라는 것
        count = len( winLoseCount[i][0] ) + len( winLoseCount[i][1] )
        if count == n-1: answer+=1
    
    return answer