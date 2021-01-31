# 16562번: 친구비
def getGroupMaster( i ):
    if group[i] == i: return i
    else: return getGroupMaster( group[i] )
    
########################################################

N, M, k = list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
group = [ i for i in range(N+1) ]

for i in range(M):
    a, b = list(map(int, input().split()))
    aMaster = getGroupMaster(a)
    bMaster = getGroupMaster(b)
    if aMaster == bMaster:
        continue
        
    if aMaster < bMaster:
        cost[aMaster] = min( cost[aMaster], cost[ bMaster ] )
        group[ bMaster ] = group[a] = group[b] = aMaster
    else:
        cost[bMaster] = min( cost[aMaster], cost[ bMaster ] )
        group[ aMaster ] = group[a] = group[b] = bMaster

result = 0
for i in range(1, N+1):
    if group[i] == i:
        result += cost[i]

if result > k:
    print( "Oh no" )
else:
    print( result )