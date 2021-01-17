# 20544번: 공룡게임

def sol( befor, now, n, isTwoValue ):
    global MOD_NUM
    if dp[ befor ][ now ][ n ][ isTwoValue ] == -1:
        a1, a2, a3 = 0, 0, 0
        
        if befor == 0 and now == 0:
            a1 = sol( now, 0, n-1, isTwoValue )
            a2 = sol( now, 1, n-1, isTwoValue )
            a3 = sol( now, 2, n-1, True )
        elif befor == 0 and now == 1:
            a1 = sol( now, 0, n-1, isTwoValue )
            a2 = sol( now, 1, n-1, isTwoValue )
            a3 = sol( now, 2, n-1, True )
        elif befor == 0 and now == 2:
            a1 = sol( now, 0, n-1, isTwoValue )
            a2 = sol( now, 1, n-1, isTwoValue )
        elif befor == 1 and now == 0:
            a1 = sol( now, 0, n-1, isTwoValue )
            a2 = sol( now, 1, n-1, isTwoValue )
            a3 = sol( now, 2, n-1, True )
        elif befor == 1 and now == 1:
            a1 = sol( now, 0, n-1, isTwoValue )
        elif befor == 1 and now == 2:
            a1 = sol( now, 0, n-1, isTwoValue )
        elif befor == 2 and now == 0:
            a1 = sol( now, 0, n-1, isTwoValue )
            a2 = sol( now, 1, n-1, isTwoValue )
            a3 = sol( now, 2, n-1, True )
        elif befor == 2 and now == 1:
            a1 = sol( now, 0, n-1, isTwoValue )
        elif befor == 2 and now == 2:
            pass
        
        
        dp[ befor ][ now ][ n ][ isTwoValue ] = ( a1 + a2 + a3 ) % MOD_NUM
        
    return dp[ befor ][ now ][ n ][ isTwoValue ]

############################################################################################
MOD_NUM = 1000000007
N = int(input())
if N == 1:
    print( 0 )
elif N == 2:
    print( 1 )
else:
    dp = [ [[ {True:-1, False:-1} for i in range(N) ] for i in range(3) ] for i in range(3) ] # befor, now, 남은 갯수, 2존재여부
    dp[ 0 ][ 0 ][ 1 ][ False ] = 1 # 2
    dp[ 0 ][ 0 ][ 1 ][ True ] = 3 # 0, 1, 2
    dp[ 0 ][ 1 ][ 1 ][ False ] = 1 # 2
    dp[ 0 ][ 1 ][ 1 ][ True ] = 3 # 0, 1, 2
    dp[ 0 ][ 2 ][ 1 ][ True ] = 2 # 0, 1
    dp[ 1 ][ 0 ][ 1 ][ False ] = 1 # 2
    dp[ 1 ][ 0 ][ 1 ][ True ] = 3 # 0, 1, 2
    dp[ 1 ][ 1 ][ 1 ][ False ] = 0
    dp[ 1 ][ 1 ][ 1 ][ True ] = 1 # 0
    dp[ 1 ][ 2 ][ 1 ][ True ] = 1 # 0
    dp[ 2 ][ 0 ][ 1 ][ True ] = 3 # 0, 1, 2
    dp[ 2 ][ 1 ][ 1 ][ True ] = 1 # 0
    
    # 시작은 0
    result = sol( 0, 0, N-2, False ) + sol( 0, 1, N-2, False ) + sol( 0, 2, N-2, True )
    
    print( result % MOD_NUM )