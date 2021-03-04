# 1043번: 거짓말
import copy

def getGroup(i):
    if group[i]==i or group[i]==-1: return group[i]
    else: return getGroup( group[i] )
########################################################
N, M = list(map(int ,input().split()))

# 진실을 알고 있는 사람은 -1로 fix
group = [i for i in range(N+1)]
datas = list(map(int ,input().split()))
for i in range(1, datas[0]+1):
    group[ datas[i] ] = -1

partys = [ list(map(int ,input().split()))[1:] for i in range(M) ]

# 계속해서 partys를 체크하며 모든 그룹 동기화가 이뤄질때까지 while문을 돔
befor = None
while befor!=group:
    befor = copy.deepcopy( group )    
    
    for party in partys:
        headerGroup = [ getGroup(i) for i in party ]
        
        # party에 모인 사람중 작은 group으로 합침
        # party에 진실을 알고있는 사람과 속한 그룹(-1)이 있을 경우 해당 party의 모든 사람이 -1로 변경됨
        newGroup = min(headerGroup)

        for i in party: group[i] = newGroup
    

result = 0
for party in partys:
    headerGroup = [ getGroup(i) for i in party ]
    newGroup = min(headerGroup)
    
    if newGroup != -1: result+=1
print(result)