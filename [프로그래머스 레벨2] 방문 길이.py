# Summer/Winter Coding: 방문 길이

def solution(dirs):
    graph = [ [0 for i in range(11)] for i in range(11) ] 
    visited = [ [ [False, False, False, False] for i in range(11) ] for i in range(11) ]
    
    move = {
        'U' : [-1,0,0,1],
        'D' : [1,0,1,0],
        'R': [0,1,2,3],
        'L': [0,-1,3,2]
    }
    
    answer = 0
    posi, posj = 5, 5
    for d in dirs:
        wi, wj, myPos, nextPos = move[d]
        nextPosi, nextPosj = posi+wi, posj+wj
        if 0<=nextPosi<11 and 0<=nextPosj<11:
            if visited[posi][posj][myPos] == False:
                visited[posi][posj][myPos] = True
                visited[nextPosi][nextPosj][nextPos] = True
                answer += 1
                
            posi, posj = nextPosi, nextPosj
                
    return answer