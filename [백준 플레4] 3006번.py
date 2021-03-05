# 3006번: 터보소트
import sys

def initTree( left, right, node ):
    if left==right: tree[node] = 1
    else:
        mid = (left+right)//2
        tree[node] = initTree(left,mid,node*2) + initTree(mid+1,right,node*2+1)
    return tree[node]

def updateTree( left, right, node ):
    global target
    if left==right==target: tree[node]=0
    elif target<left or target > right: pass
    else:
        mid = (left+right)//2
        tree[node] = updateTree(left,mid,node*2) + updateTree(mid+1,right,node*2+1)
    return tree[node]
    
def getRangeCount( left, right, node ):
    global targetL, targetR
    if targetR < left or targetL > right: return 0
    elif targetL <= left <= right <= targetR: return tree[node]
    else:
        mid = (left+right)//2
        return getRangeCount(left,mid,node*2) + getRangeCount(mid+1,right,node*2+1)
################################################################################
N = int(input())

indexs = [ 0 for i in range(N+1) ]
for index in range(1, N+1):
    data = int(sys.stdin.readline())
    indexs[data] = index
    
tree = [0 for i in range(N*4+10)]
initTree(1, N, 1)
minV, maxV = 1, N
for i in range(1, N+1):
    if i%2==1: # 최소값 왼쪽으로
        target = indexs[minV]
        targetL, targetR = 1, target-1
        minV+=1
    else: # 최대값 오른쪽으로
        target = indexs[maxV]
        targetL, targetR = target+1, N
        maxV -= 1

    print( getRangeCount(1,N,1) )
    updateTree(1, N, 1)