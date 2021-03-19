# Summer/Winter Coding: 기지국 설치
def solution(n, stations, w):
    for i in range(len(stations)):
        stations[i] = [ stations[i]-w, stations[i]+w ]
    
    emptyPos = [ [1, stations[0][0]-1] ]
    for i in range(1, len(stations)):
        emptyPos.append( [ stations[i-1][1]+1, stations[i][0]-1 ] )
    emptyPos.append( [ stations[-1][1]+1, n ] )
    
    answer = 0
    oneLen = w*2+1
    for empty in emptyPos:
        emptyLen = empty[1] - empty[0] + 1
        if emptyLen <= 0: continue
        
        answer += 1
        answer += (emptyLen-1) // oneLen
    
    return answer