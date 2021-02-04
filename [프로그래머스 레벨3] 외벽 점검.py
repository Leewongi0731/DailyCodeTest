# 2020 카카오 공채: 외벽 점검
from bisect import bisect_left
import copy
import sys

def sol( n, weak, dist, i, startIndex, distCheck, count ):
    weakIndex = bisect_left(weak, i)
    
    # 더이상 확인 할 취약지점이 없음
    if weakIndex == len(weak):  
        if startIndex == 0:
            return count
        elif startIndex < len(weak) and i > weak[startIndex-1] + n:
            return count
        else:
            return sys.maxsize

    tmp = [ sys.maxsize ]
    if weakIndex == startIndex:
        # 해당 지점말고, 다음지점에서 시작하고 싶을 경우
        tmp.append( sol( n, weak, dist, weak[weakIndex]+1, startIndex+1, distCheck, 0 ) )
        
        for distIndex in range( len(distCheck) ):
            check = copy.deepcopy( distCheck )
            check[ distIndex ] = 1
            tmp.append( sol( n, weak, dist, weak[weakIndex]+dist[distIndex]+1, startIndex, check, 1 ) )
    else:
        for distIndex in range( len(distCheck) ):
            # 이미 앞에서 사용함
            if distCheck[distIndex] == 1:  continue
                
            check = copy.deepcopy( distCheck )
            check[ distIndex ] = 1
            tmp.append( sol( n, weak, dist, weak[weakIndex]+dist[distIndex]+1, startIndex, check, count+1 ) )
    return min(tmp)
###################################################################################

def solution(n, weak, dist):
    if len(weak) == 1: return 1    
    
    answer = sol( n, weak, dist, -1, 0, [0 for i in range(len(dist))], 0 )
    
    if answer == sys.maxsize: return -1
    return answer