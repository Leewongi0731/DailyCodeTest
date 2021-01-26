# 10868번: 최솟값
import sys

MAX_VALUE = 1234567890

def initTree( left, right, node ):
    if left==right: 
        minSegmentTree[node] = datas[left]
        return minSegmentTree[node]
    else:
        mid = ( left + right ) // 2
        minSegmentTree[node] = min( initTree(left, mid, node*2) , initTree(mid+1, right, node*2+1) )
        return minSegmentTree[node]
def getRangeMinValue( left, right, node ):
    global targetLeft, targetRight, MAX_VALUE
    if targetLeft > right or targetRight < left: return MAX_VALUE
    elif targetLeft <= left and targetRight >= right: return minSegmentTree[node]
    else:
        mid = ( left + right ) // 2
        return min( getRangeMinValue( left, mid, node*2 ), getRangeMinValue( mid+1, right, node*2+1 ) )
##################################################################
N, M = list(map(int, input().split()))
datas = [0] + [ int( sys.stdin.readline() ) for i in range(N) ]
minSegmentTree = [ -1 for i in range(N*4+20) ]
initTree( 1, N, 1 )

for _ in range(M):
    targetLeft, targetRight = list(map(int, sys.stdin.readline().split()))
    print( getRangeMinValue( 1, N, 1 ) )