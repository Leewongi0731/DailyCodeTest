# 10775번: 공항
# PyPy3로 제출하면 메모리초과... 
# Python3로 제출하면 통과

import sys
sys.setrecursionlimit(10**6)

def getPosition( i ):
    if position[i] == i: return i
    else: return getPosition( position[i] )
##############################################################
G = int(input())
P = int(input())
datas = [ int(sys.stdin.readline()) for i in range(P) ]
position = [ i for i in range(G+1) ]
result = 0
for i, data in enumerate( datas ):
    insertGate = getPosition( data )
    if insertGate == 0:break
    
    position[ data ] = position[ insertGate - 1 ]
    position[ insertGate ] =  position[ insertGate - 1 ]
    result += 1
print( result )