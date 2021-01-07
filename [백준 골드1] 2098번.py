# 2098번: 외판원 순회
# MAX VALUE를100000000000000000 처음 큰 수로 하면 J.N에서는 되는데, 백준 서버에서 오버플로우 되는 듯 함..
# MAX VALUE -> 987654321로 수정

def TSP( N, graph ):
    stat = 1
    now = 0
    finishStat = pow(2,N) - 1
    
    dp[ stat ][ now ] = getMinCost( stat, now, graph, finishStat )
    
    return dp[ stat ][ now ]

def getMinCost( stat, now, graph, finishStat ): # 해당위치(now)에서 순회하기 위한 가장 짧은 루트의 COST
    if stat == finishStat:
        if graph[ now ][ 0 ] == 0: # unconnect
            return 987654321  # max Value
        return graph[ now ][ 0 ] # connect
    
    costList = []
    for i, cost in enumerate( graph[ now ] ):
        if cost == 0: # unconnect
            continue
        
        bitMast = bitMasts[ i ]
        if stat == stat|bitMast: # vistied
            continue
        
        if dp[ stat|bitMast ][ i ] == 0:
            dp[ stat|bitMast ][ i ] = getMinCost( stat|bitMast, i, graph, finishStat)
        costList.append( dp[ stat|bitMast ][ i ] + cost ) 
    
    if len( costList ) == 0:
        return 987654321 # max Value
    else:
        return min( costList )

########################################################################################
N = int(input())
graph = [ [] for i in range( N ) ]
for i in range(N):
    graph[ i ] = list( map(int, input().split()) )
    
dp = [ [0 for i in range(N) ] for j in range(pow(2,N)) ]
bitMasts = [ pow(2, i) for i in range(N) ]
print( TSP( N, graph ) )