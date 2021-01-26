# 14438번: 수열과 쿼리 17
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
    
def updateTree( left, right, node ):
    global targetIndex
    if targetIndex < left or targetIndex > right: return minSegmentTree[node]
    elif left == right == targetIndex:
        minSegmentTree[node] = datas[targetIndex]
        return minSegmentTree[node]
    else:
        mid = ( left + right ) // 2
        minSegmentTree[node] = min( updateTree(left, mid, node*2), updateTree(mid+1, right, node*2+1) )
        return minSegmentTree[node]
    
def getRangeMinValue( left, right, node ):
    global targetLeft, targetRight, MAX_VALUE
    if targetLeft > right or targetRight < left: return MAX_VALUE
    elif targetLeft <= left and targetRight >= right: return minSegmentTree[node]
    else:
        mid = ( left + right ) // 2
        return min( getRangeMinValue( left, mid, node*2 ), getRangeMinValue( mid+1, right, node*2+1 ) )
##################################################################
N = int(input())
datas = [0] + list(map(int, sys.stdin.readline().split()))
minSegmentTree = [ -1 for i in range(N*4+20) ]
initTree( 1, N, 1 )

M = int(input())
for _ in range(M):
    a,b,c = list(map(int, sys.stdin.readline().split()))
    if a == 1:
        targetIndex, updateValue = b, c
        datas[targetIndex] = updateValue
        updateTree(1, N, 1)
    else:
        targetLeft, targetRight = b, c
        print( getRangeMinValue( 1, N, 1 ) )