# 14427번: 수열과 쿼리 15
import sys

def initTree(left, right, node):
    if left==right: tree[node] = [datas[left], left ] # value, index
    else:
        mid = (left+right)//2
        leftTree = initTree(left, mid, node*2)
        rightTree = initTree(mid+1, right, node*2+1)
        
        if leftTree[0] <= rightTree[0]:
            tree[node] = [ leftTree[0], leftTree[1] ]
        else:
            tree[node] = [ rightTree[0], rightTree[1] ]
    return tree[node]

def updateTree( left, right, node):
    global target, num
    if target < left or target > right: pass
    elif left==right==target:tree[node] = [ num, target ] # value, index
    else:
        mid = (left+right)//2
        leftTree = updateTree(left, mid, node*2)
        rightTree = updateTree(mid+1, right, node*2+1)
        
        if leftTree[0] <= rightTree[0]:
            tree[node] = [ leftTree[0], leftTree[1] ]
        else:
            tree[node] = [ rightTree[0], rightTree[1] ]
    return tree[node]

def getRangeMultiply( left, right, node ):
    global targetL, targetR
    if targetR < left or targetL > right: return [ 10**10, N ] # 나오지 않는 최대 값
    elif targetL <= left and right <= targetR: return tree[node]
    else:
        mid = (left+right)//2
        leftTree = getRangeMultiply(left, mid, node*2)
        rightTree = getRangeMultiply(mid+1, right, node*2+1)
        
        if leftTree[0] <= rightTree[0]: return leftTree
        else: return rightTree
########################################################################
N = int(input())
datas = [0] + list(map(int, input().split()))

tree = [ 0 for i in range(N*4+10) ]
initTree(1, N, 1)

M = int(input())
for _ in range(M):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] == 1: # 1 i v : Ai를 v로 바꾼다.
        target, num = query[1], query[2]
        updateTree(1, N, 1)
        
    else: # 2 : 전 범위에서 가장 작은 값의 인덱스를 출력
        targetL, targetR = 1, N
        value, index = getRangeMultiply(1, N, 1)
        print( index )