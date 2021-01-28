# 13537번 수열과 쿼리 1
# 세그먼트 트리에 모든 노드를 정렬해놓은 상태에서, 특정 범위 퀴리가 들어오면 binary search로 갯수를 찾아 합침
# segment tree + merge sort + binary search
import sys
from bisect import bisect_right #이진탐색 코드

def initTree( left, right, node ):
    if left == right:
        tree[node].append( datas[left] )
        return tree[node]
    else:
        mid = (left + right) // 2
        tree[node] = initTree( left, mid, node*2 ) + initTree( mid+1, right, node*2+1 )
        return tree[node]

def getRangeUpCount( left, right, node ):
    global rangeLeft, rangeRight, value
    if rangeLeft > right or rangeRight < left: return 0
    elif rangeLeft <= left and  right <= rangeRight: 
        return len(tree[node]) - bisect_right(tree[node], value)
    else:
        mid = (left + right) // 2
        return getRangeUpCount( left, mid, node*2 ) + getRangeUpCount( mid+1, right, node*2+1 )
########################################################
N = int(input())
datas = [0] + list( map(int, sys.stdin.readline().split()) )

tree = [ [] for i in range(300000) ]
initTree( 1, N, 1 )

for i in range(300000):
    if tree[i] != []: tree[i].sort()

M = int(input())
for _ in range(M):
    rangeLeft, rangeRight, value = list( map(int, sys.stdin.readline().split()) )
    print( getRangeUpCount(1, N, 1) ) 