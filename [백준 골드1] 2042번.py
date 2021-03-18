# 2042번: 구간 합 구하기

# 풀이1 : FenwickTree이용
def updateFenwickTree( i, diff ):
    global N
    while i <= N:
        fenwickTree[i] += diff
        i += (i & -i) # 마지막 1에 1추가
        
def getSumFenwickTree( i ):
    ans = 0
    while i > 0:
        ans += fenwickTree[i]
        i -= (i & -i) # 마지막 1제거
    return ans

#################################################################
N, M, K = list(map(int, input().split()))
datas = [0] + [ int(input()) for i in range(N) ]

fenwickTree = [0 for i in range(N+1)]

# init fenwickTree
for i in range(1, N+1):
    data = datas[i]
    updateFenwickTree( i, data )


for _ in range(M+K):
    a,b,c = list(map(int, input().split()))
    if a == 1:
        beforData = datas[b]
        afterData = c
        
        diff = afterData - beforData
        updateFenwickTree( b, diff )
        datas[b] = c
    else:
        rangeSum = getSumFenwickTree( c ) - getSumFenwickTree( b-1 )
        print( rangeSum )

'''
# 풀이 2: Segment Tree이용
def initTree( left, right, node ):
    if left==right: 
        tree[node] = datas[left]
        return tree[node]
    else:
        mid = ( left + right ) // 2
        tree[node] = initTree(left, mid, node*2) + initTree(mid+1, right, node*2+1)
        return tree[node]

def updateTree( left, right, node ):
    global targetIndex
    if targetIndex < left or targetIndex > right: return tree[node]
    elif left == right == targetIndex:
        tree[node] = datas[targetIndex]
        return tree[node]
    else:
        mid = ( left + right ) // 2
        tree[node] = updateTree(left, mid, node*2) + updateTree(mid+1, right, node*2+1)
        return tree[node]

def getRangeSum( left, right, node ):
    global targetLeft, targetRight
    if targetLeft > right or targetRight < left: return 0
    elif targetLeft <= left and targetRight >= right: return tree[node]
    else:
        mid = ( left + right ) // 2
        return getRangeSum( left, mid, node*2 ) + getRangeSum( mid+1, right, node*2+1 )
        
################################################################################
N, M, K = list(map(int, input().split()))
datas = [0] + [ int(input()) for i in range(N) ]
tree = [ -1 for i in range(N*4+20) ]
initTree( 1, N, 1 )

for _ in range(M+K):
    a,b,c = list(map(int, input().split()))
    if a == 1:
        targetIndex, updateValue = b, c
        datas[targetIndex] = updateValue
        updateTree(1, N, 1)
    else:
        targetLeft, targetRight = b, c
        print( getRangeSum( 1, N, 1 ) )
'''