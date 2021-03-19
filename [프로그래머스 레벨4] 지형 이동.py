# Summer/Winter Coding: 지형 이동
def getGroupID( N, group, i, j  ):
    node = i*N+j
    if group[i][j] != node:
        pi, pj = group[i][j] // N, group[i][j] % N
        return getGroupID( N, group, pi, pj  )
    else: return node

def solution(land, height):
    N = len(land)
    
    linkCost = []
    mx, my = [1,0], [0,1]
    for i in range(N):
        for j in range(N):
            for z in range(2):
                ii,jj=i+mx[z], j+my[z]
                if ii<N and jj<N:
                    cost = abs(land[i][j] - land[ii][jj])
                    if cost <= height: cost = 0
                    
                    linkCost.append( [ cost, i, j, ii, jj ] ) # cost, i, j, ii, jj
    
    linkCost = sorted( linkCost )
    
    group = [ ]
    for i in range(N):
        group.append( [ n for n in range( i*N, i*N+N ) ] )
    
    answer = 0
    for cost, i, j, ii, jj in linkCost:
        g1, g2 = getGroupID( N, group, i, j  ), getGroupID( N, group, ii, jj  )
        if g1 != g2:
            g1pi, g1pj = g1 // N, g1 % N
            g2pi, g2pj = g2 // N, g2 % N
            
            if g1 < g2: # g1으로 통합
                group[i][j] = group[ii][jj] = group[g1pi][g1pj] = group[g2pi][g2pj] = g1
            else: # g2으로 통합
                group[i][j] = group[ii][jj] = group[g1pi][g1pj] = group[g2pi][g2pj] = g2
            
            answer += cost

    return answer 