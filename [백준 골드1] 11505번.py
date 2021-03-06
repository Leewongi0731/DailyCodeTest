# 11505번: 구간 곱 구하기
import sys

def initTree(left, right, node):
    if left==right: tree[node] = datas[left]
    else:
        mid = (left+right)//2
        tree[node] = ( initTree(left, mid, node*2) * initTree(mid+1, right, node*2+1) ) % 1000000007
    return tree[node]

def updateTree( left, right, node):
    global target, num
    if target < left or target > right: pass
    elif left==right==target:tree[node]=num
    else:
        mid = (left+right)//2
        tree[node] = ( updateTree(left, mid, node*2) * updateTree(mid+1, right, node*2+1) ) % 1000000007
    return tree[node]

def getRangeMultiply( left, right, node ):
    global targetL, targetR
    if targetR < left or targetL > right: return 1
    elif targetL <= left and right <= targetR: return tree[node]
    else:
        mid = (left+right)//2
        return ( getRangeMultiply(left, mid, node*2) * getRangeMultiply(mid+1, right, node*2+1) ) % 1000000007
########################################################################
N, M, K = list(map(int, input().split()))
datas = [0] + [ int(sys.stdin.readline()) for i in range(N) ]

tree = [ 0 for i in range( N*4+1 ) ]
initTree(1, N, 1)

for _ in range(M+K):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    if a == 1: # b번째를 c로 변경
        target, num = b, c
        updateTree( 1, N, 1 )
    else: # b~c까지의 곱
        targetL, targetR = b, c
        v = getRangeMultiply( 1, N, 1 )
        print( v )