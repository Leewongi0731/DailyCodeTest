# 2357번: 최솟값과 최댓값
import sys
sys.setrecursionlimit(10**8) 

def initTree( left, right, node ):
    if left==right:
        tree[node] = [datas[left], datas[left]]
        return tree[node]
    else:
        mid = (left+right) // 2
        
        r1 = initTree( left, mid, node*2 )
        r2 = initTree( mid+1, right, node*2+1 )
        tree[node] = [  min(r1[0], r2[0]),  max(r1[1],r2[1])  ]
        return tree[node] 
        
def findMinMaxValue( left, right, node ):
    global findLeft, findRight
    if right < findLeft or findRight < left:
        return [1000000001, 0] # 존재하지 않은 수
    elif findLeft <= left and right <= findRight:
        return tree[node]
    else:
        mid = (left+right) // 2
        r1 = findMinMaxValue( left, mid, node*2 )
        r2 = findMinMaxValue( mid+1, right, node*2+1 )
        return [  min(r1[0], r2[0]),  max(r1[1],r2[1])  ]
    
############################################################

N, M = list(map(int, input().split()))
datas = [0] + [ int(sys.stdin.readline()) for i in range(N) ]
tree=[ [] for i in range( N*4 + 20 ) ]
initTree(1, N, 1)

for _ in range(M):
    findLeft, findRight = list(map(int, sys.stdin.readline().split()))
    
    minVal, maxVal = findMinMaxValue(1, N, 1)
    
    print( minVal, maxVal )