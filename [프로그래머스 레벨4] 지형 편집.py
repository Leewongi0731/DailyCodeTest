# Summer/Winter Coding: 지형 편집
from collections import Counter

def solution(land, P, Q):
    N = len(land)
    
    allLand = []
    for l in land:  allLand += l
    counter = Counter( allLand )
    layers = sorted( list( counter.keys() ) )
    
    layer = layers[0]
    # up / down
    areaCount = [0, N*N-counter[layer]]
    blockCount = [ 0, 0 ]
    for c in counter:
        blockCount[1] += counter[c] * ( c-layer )
    
    answer = blockCount[0]*P + blockCount[1]*Q
    for nextLayer in layers[1:]:        
        # 한층 올라가면, 올라가는 area 갯수가 증가하고, 그 만큼 쌓아야하는 block수가 증가함
        areaCount[0] += counter[layer]
        blockCount[0] += areaCount[0] * ( nextLayer - layer )
        
        # 한층 올라가면, 내려야하는 block수가 감소하고, 현재 층 갯수만큼 내려가는 area 갯수가 감소함
        blockCount[1] -= areaCount[1] * ( nextLayer - layer )
        areaCount[1] -= counter[nextLayer]
        
        answer = min( answer, blockCount[0]*P + blockCount[1]*Q )
        layer = nextLayer
    return answer